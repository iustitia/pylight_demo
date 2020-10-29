from rest_framework.test import APITestCase


class ApiTests(APITestCase):

    def test_ok(self):
        response = self.client.get("/api/v3/pokemon/")
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json(), [])

    def _test_create(self, arg, status_code):
        response = self.client.post("/api/v3/pokemon/", data=arg)
        self.assertEquals(response.status_code, status_code)
        return response

    def test_create_ok(self):
        response = self._test_create({"name": "test"}, 201)
        self.assertIn("test", str(response.content))

    def test_create_missing_name(self):
        response = self._test_create({"id": "test"}, 400)
        self.assertEquals(response.json()["name"][0], "This field is required.")
