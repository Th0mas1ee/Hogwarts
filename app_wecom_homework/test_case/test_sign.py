from app_wecom_homework.pages.app import App


class TestSign:
    def setup(self):
        self.app = App()

    def test_sign(self):
        self.app.goto_main().goto_workspace_page().goto_sign_page().sign()

    def test_first_sign(self):
        self.app.goto_main().goto_workspace_page().goto_sign_page().first_sign()