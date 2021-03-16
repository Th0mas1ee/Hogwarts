from framework_practice.pages.add_member_page import AddMemberPage
from framework_practice.pages.basepage import BasePage
from framework_practice.pages.contact_pages.search_contact_page import SearchContactPage


class ContactPage(BasePage):
    def goto_add_member_page(self):
        self.parse_action('../pages/contact_pages/contact_page.yaml', 'goto_add_member_page')
        return AddMemberPage(self.driver)

    def get_contact_names(self):
        # self.driver.refresh()
        eles = self.parse_action('../pages/contact_pages/contact_page.yaml', 'get_contact_names')
        # print(len(eles))
        names = []
        for ele in eles[1:-1]:
            name = ele.get_attribute('text')
            names.append(name)
            # print(f"name: {name}")
        return names

    def goto_search_contact_page(self):
        self.parse_action('../pages/contact_pages/contact_page.yaml', 'goto_search_contact_page')
        return SearchContactPage(self.driver)
