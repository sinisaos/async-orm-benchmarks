from locust import HttpUser, task


class Benchmark(HttpUser):
    @task
    def tag_list_bench(self):
        self.client.get("/small-table/")

    @task
    def tag_single_bench(self):
        self.client.get("/small-table/1/")

    @task
    def question_list_bench(self):
        self.client.get("/related-table/")

    @task
    def question_single_bench(self):
        self.client.get("/related-table/1/")

    @task
    def mega_table_list_bench(self):
        self.client.get("/mega-table/")

    @task
    def mega_table_single_bench(self):
        self.client.get("/mega-table/1/")
