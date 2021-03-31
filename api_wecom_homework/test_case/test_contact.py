# 编写通讯录测试用例（利用数据清洗）
# 利用 session 封装通讯录基本操作
import pytest

from api_wecom_homework.wecom.contact import Contact


class TestContact:
    def setup(self):
        self.contact = Contact()

    @pytest.mark.parametrize("user_id, name, mobile, department", [
        ("test_id001", "test_name001", "13812300001", [1]),
        ("test_id002", "test_name002", "13812300002", [1]),
        ("test_id003", "test_name003", "13812300003", [1]),
        ("test_id004", "test_name004", "13812300004", [1]),
        ("test_id005", "test_name005", "13812300005", [1]),
        ("test_id006", "test_name006", "13812300006", [1]),
        ("test_id007", "test_name007", "13812300007", [1]),
        ("test_id008", "test_name008", "13812300008", [1]),
        ("test_id009", "test_name009", "13812300009", [1]),
    ])
    def test_create_member(self, user_id, name, mobile, department):
        self.contact.delete_member(user_id)
        r = self.contact.create_member(user_id, name, mobile, department)
        # print(f"****{r.get('errmsg', 'network error')}")
        assert r.get('errmsg', "network error") == "created"
        r = self.contact.get_member_info(user_id)
        self.contact.delete_member(user_id)
        assert r.get("name") == name

    @pytest.mark.parametrize("user_id, name, mobile, department", [
        ("test_id001", "test_name001", "13812300001", [1]),
        ("test_id002", "test_name002", "13812300002", [1]),
        ("test_id003", "test_name003", "13812300003", [1]),
        ("test_id004", "test_name004", "13812300004", [1]),
        ("test_id005", "test_name005", "13812300005", [1]),
        ("test_id006", "test_name006", "13812300006", [1]),
        ("test_id007", "test_name007", "13812300007", [1]),
        ("test_id008", "test_name008", "13812300008", [1]),
        ("test_id009", "test_name009", "13812300009", [1]),
    ])
    def test_get_member_info(self, user_id, name, mobile, department):
        self.contact.create_member(user_id, name, mobile, department)
        r = self.contact.get_member_info(user_id)
        self.contact.delete_member(user_id)
        assert r.get("errmsg") == "ok"
        assert r.get("name") == name

    @pytest.mark.parametrize("user_id, name, mobile, department", [
        ("test_id001", "test_name001", "13812300001", [1]),
        ("test_id002", "test_name002", "13812300002", [1]),
        ("test_id003", "test_name003", "13812300003", [1]),
        ("test_id004", "test_name004", "13812300004", [1]),
        ("test_id005", "test_name005", "13812300005", [1]),
        ("test_id006", "test_name006", "13812300006", [1]),
        ("test_id007", "test_name007", "13812300007", [1]),
        ("test_id008", "test_name008", "13812300008", [1]),
        ("test_id009", "test_name009", "13812300009", [1]),
    ])
    def test_delete_member(self, user_id, name, mobile, department):
        self.contact.create_member(user_id, name, mobile, department)
        r = self.contact.delete_member(user_id)
        assert r.get("errmsg") == "deleted"
        r = self.contact.get_member_info(user_id)
        assert r.get("errcode") == 60111

    @pytest.mark.parametrize("user_id, name, mobile, department", [
        ("test_id001", "test_name001", "13812300001", [1]),
        ("test_id002", "test_name002", "13812300002", [1]),
        ("test_id003", "test_name003", "13812300003", [1]),
        ("test_id004", "test_name004", "13812300004", [1]),
        ("test_id005", "test_name005", "13812300005", [1]),
        ("test_id006", "test_name006", "13812300006", [1]),
        ("test_id007", "test_name007", "13812300007", [1]),
        ("test_id008", "test_name008", "13812300008", [1]),
        ("test_id009", "test_name009", "13812300009", [1]),
    ])
    def test_update(self, user_id, name, mobile, department):
        self.contact.delete_member(user_id)
        self.contact.create_member(user_id, name, mobile, department)
        new_name = name + "tmp"
        r = self.contact.update_member(user_id, new_name, mobile)
        assert r.get("errmsg") == "updated"
        r = self.contact.get_member_info(user_id)
        self.contact.delete_member(user_id)
        assert r.get("name") == new_name
