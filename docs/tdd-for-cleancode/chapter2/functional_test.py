from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 유저가 해당 웹사이트를 접속
        self.browser.get('http://localhost:8000')

        # 웹 페이지 타이틀과 헤더가 To-Do로 표시하고 있음
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        
        # 해당 사이트를 이용한다

        # 어쩌구 저쩌구 버튼을 클릭해서 어쩌구 저쩌구 해서
        # 이렇궁 저렇궁 되면
        # 요롷게 저렇게 한다

        # 사용이 끝나면 브라우저를 종료한다

if __name__ == '__main__':
    unittest.main(warnings='ignore')


