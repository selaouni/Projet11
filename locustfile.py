from locust import HttpUser, TaskSet, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task(10)
    def index(self):
        self.client.get("/")

    @task(10)
    def on_stop(self):
        self.client.get('/logout')

    @task(5)
    def purchase_places(self):
        self.client.get('/purchasePlaces')

    @task(5)
    def points(self):
        self.client.get("/points_dashboard")

    @task(10)
    def show_summary(self):
        self.client.get('/showSummary')