import unittest

from fastapi.testclient import TestClient

from app import app


class TextStatsApiTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app, raise_server_exceptions=False)
        self.addCleanup(self.client.close)

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_stats_counts_characters_words_and_lines(self):
        cases = [
            ("hello", {"characters": 5, "words": 1, "lines": 1}),
            ("", {"characters": 0, "words": 0, "lines": 0}),
            ("one  two\tthree", {"characters": 14, "words": 3, "lines": 1}),
            ("café\r\n🦊", {"characters": 7, "words": 2, "lines": 2}),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                response = self.client.post("/stats", json={"text": text})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json(), expected)

    def test_stats_rejects_invalid_input(self):
        for payload in ({}, {"text": 42}, {"text": "a" * 20_001}):
            with self.subTest(keys=tuple(payload), value_type=type(payload.get("text"))):
                response = self.client.post("/stats", json=payload)
                self.assertEqual(response.status_code, 422)
