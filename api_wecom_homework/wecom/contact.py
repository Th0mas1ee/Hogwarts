from api_wecom_homework.wecom.base import BaseApi


class Contact(BaseApi):
    def create_member(self, user_id, name, mobile, department):
        create_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
            'department': department
        }
        r = self.send('POST', url=create_url, json=data)
        return r.json()

    def get_member_info(self, user_id):
        get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        params = {
            "userid": user_id
        }
        r = self.send("GET", get_member_url, params=params)
        return r.json()

    def update_member(self, user_id, name, mobile):
        update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
        }
        r = self.send("POST", url=update_member_url, json=data)
        return r.json()

    def delete_member(self, user_id):
        delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        params = {"userid": user_id}
        r = self.send("GET", delete_url, params=params)
        return r.json()