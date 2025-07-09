class DownloadReportApiView(APIView):
    permission_classes = [IsAuthenticated]

    class Echo:
        """A pseudo-buffer for streaming CSV rows."""
        def write(self, value):
            return value

    def fetch_info(self, pk, user):
        campaign = get_object_or_404(
            CampaingModel.active.annotate(
                total_numbers=Count("action_campaign"),
                notstarted=Count("action_campaign", filter=Q(action_campaign__status="not started")),
                completed=Count("action_campaign", filter=Q(action_campaign__status="completed")),
                hungup=Count("action_campaign", filter=Q(action_campaign__status="hungup")),
                failed=Count("action_campaign", filter=Q(action_campaign__status="failed")),
                unanswered=Count("action_campaign", filter=Q(action_campaign__status="unanswered")),
                terminated=Count("action_campaign", filter=Q(action_campaign__status="terminated")),
                total_credit_consumed=Sum("action_campaign__credit_consumed")
            ),
            pk=pk, 
            user=user,
            deleted_at__isnull=True
        )
        percent_not_started = 0
        success_rate = 0
        failure_rate = 0
        total_calls_made = campaign.total_numbers - campaign.notstarted

        if total_calls_made > 0:
            successful_calls = campaign.completed + campaign.hungup
            success_rate = (successful_calls / total_calls_made) * 100

            failed_calls = campaign.failed + campaign.unanswered + campaign.terminated
            failure_rate = (failed_calls / total_calls_made) * 100

        if campaign.total_numbers:
            percent_not_started = (campaign.notstarted / campaign.total_numbers) * 100
            percent_completed = (campaign.completed / campaign.total_numbers) * 100

        info = {
            "campaign_name": campaign.name or "",
            "services": campaign.services or "",
            "message": campaign.message or "",
            "description": campaign.description or "",
            "status": campaign.status,
            "total_numbers": campaign.total_numbers,
            "not_started_count": campaign.notstarted,
            "not_started": f"{percent_not_started:.2f}%",
            "completed_count": campaign.completed,
            "completed": f"{percent_completed:.2f}%",
            "success_count": campaign.completed + campaign.hungup if total_calls_made > 0 else 0,
            "success_rate": f"{success_rate:.2f}%",
            "failure_count": campaign.failed + campaign.unanswered + campaign.terminated if total_calls_made > 0 else 0,
            "failure_rate": f"{failure_rate:.2f}%",
            "total_credit_consumed": campaign.total_credit_consumed or 0
        }

        return campaign, info

    def stream_content(self, info, details_qs):
        yield ["Campaign Name", str(info.get("campaign_name"))]
        yield ["Services", str(info.get("services"))]
        yield ["Message", str(info.get("message"))]
        yield ["Description", str(info.get("description"))]
        yield ["Status", str(info.get("status"))]
        yield [""]
        yield ["Total Numbers", str(info.get("total_numbers"))]
        yield ["Not Started", str(info.get("not_started")), str(info.get("not_started_count"))]
        yield ["Completed", str(info.get("completed")), str(info.get("completed_count"))]
        yield [""]
        yield ["Success Rate", str(info.get("success_rate")), str(info.get("success_count"))]
        yield ["Failure Rate", str(info.get("failure_rate")), str(info.get("failure_count"))]
        yield ["Total Credit Consumed", str(info.get("total_credit_consumed"))]
        yield [""]
        yield ["Number", "Status", "Duration (Seconds)", "Playback (%)", "Credit Consumed", "Other Info", "Action Date", "Carrier"]

        for detail in details_qs:
            yield [
                detail.number,
                detail.status,
                detail.duration,
                detail.playback,
                detail.credit_consumed,
                detail.other_variables,
                detail.updated_at,
                detail.get_carrier
            ]

    def get(self, request, pk, *args, **kwargs):
        campaign, info = self.fetch_info(pk, request.user)

        # Stream large dataset using iterator to avoid memory overflow
        details_qs = campaign.action_campaign.filter(deleted_at__isnull=True).iterator()

        pseudo_buffer = DownloadReportApiView.Echo()
        writer = csv.writer(pseudo_buffer)

        response = StreamingHttpResponse(
            (writer.writerow(row) for row in self.stream_content(info, details_qs)),
            content_type="text/csv"
        )
        response["Content-Disposition"] = f'attachment; filename="{info.get("campaign_name", "campaign_report")}.csv"'

        set_audit("Campaign","Download Report")
        campaign.save()
        return response