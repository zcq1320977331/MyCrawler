from get_all_publisher_urls import GetPubUrl
from get_all_book_urls import GetBookUrls
from get_book_info import GetBookInfo

class Updata_DB(object):
    def __init__(self,ip_pool=None):
        self.pool = ip_pool
    def updata(self):
        #更新出版社信息url
        get_pub_urs = GetPubUrl()
        get_pub_urs.get_all_data()

        # 更新书籍url
        get_book_urls = GetBookUrls(self.pool)
        get_book_urls.get_all_data()

        #更新书籍信息
        get_book_info = GetBookInfo(self.pool)
        get_book_info.get_all_data()

if __name__ == '__main__':
    updata_db = Updata_DB
    updata_db.updata()