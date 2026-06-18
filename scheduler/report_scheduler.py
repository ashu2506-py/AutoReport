from apscheduler.schedulers.blocking import BlockingScheduler


class ReportScheduler:

    def start(self, task):

        scheduler = BlockingScheduler()

        scheduler.add_job(
            task,
            trigger="interval",
            minutes=1
        )

        print("Scheduler Started...")
        print("Generating report every minute")

        scheduler.start()