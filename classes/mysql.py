from config import IMPOSPACE_MYSQL_SERVER, STAT_MYSQL_SERVER
from sqlalchemy import *
from datetime import datetime


class MySqlFactory:
    impospace_server = create_engine(IMPOSPACE_MYSQL_SERVER, echo=False, convert_unicode=True)
    stat_server = create_engine(STAT_MYSQL_SERVER, echo=False, convert_unicode=True)

    @staticmethod
    def get_websites_table(network_name):
        if type(network_name) is str:
            table_name = "network_" + network_name
        else:
            return None

        try:
            table = Table(table_name, MetaData(bind=MySqlFactory.stat_server), autoload=True)
        except Exception:
            table = Table(table_name, MetaData(bind=MySqlFactory.stat_server),
                          Column("id", Integer, primary_key=True),
                          Column("name", String(255), nullable=True),
                          Column("site_id", String(255), nullable=True),
                          Column("impressions", Integer, nullable=True),
                          Column("clicks", Integer, nullable=True),
                          Column("ctr", Float, nullable=True),
                          Column("revenue", Float, nullable=True),
                          Column("ecpm", Float, nullable=True),
                          Column("date_created", DateTime(timezone=False), nullable=True, default=datetime.utcnow()), mysql_engine="InnoDB")
            table.create(checkfirst=True)
        return table

    @staticmethod
    def get_websites_table():
        table_name = "websites"
        try:
            table = Table(table_name, MetaData(bind=MySqlFactory.stat_server), autoload=True)
        except Exception:
            table = Table(table_name, MetaData(bind=MySqlFactory.stat_server),
                          Column("id", Integer, primary_key=True),
                          Column("site_id", String(255), nullable=True),
                          Column("domain", String(255), nullable=True),
                          Column("date", String(255), nullable=True),

                          Column("total_page_views", Integer, nullable=True),
                          Column("adblocked_page_views", Integer, nullable=True),

                          Column("pops_impressions", Integer, nullable=True),
                          Column("pops_revenue", Float, nullable=True),
                          Column("pops_ecpm", Float, nullable=True),

                          Column("display_impressions", Integer, nullable=True),
                          Column("display_clicks", Integer, nullable=True),
                          Column("display_ctr", Float, nullable=True),
                          Column("display_revenue", Float, nullable=True),
                          Column("display_ecpm", Float, nullable=True),

                          Column("total_revenue", Float, nullable=True),

                          Column("date_created", DateTime(timezone=False), nullable=True, default=datetime.utcnow()),
                          mysql_engine="InnoDB")
            table.create(checkfirst=True)
        return table

    @staticmethod
    def get_getjs_table():
        current_date = datetime.utcnow().strftime("%Y_%m_%d")
        table_name = "get_js_{0}".format(current_date)
        try:
            table = Table(table_name, MetaData(bind=MySqlFactory.impospace_server), autoload=True)
        except Exception:
            table = Table(table_name, MetaData(bind=MySqlFactory.impospace_server),
                          Column("id", Integer, primary_key=True),
                          Column("site_id", String(255), nullable=True),
                          Column("sub_id", String(255), nullable=True),
                          Column("user_id", String(255), nullable=True),
                          Column("country_code", String(255), nullable=True),
                          Column("ip", String(255), nullable=True),
                          Column("user_agent", Text(), nullable=True),
                          Column("referer", Text(), nullable=True),
                          Column("referer_domain", String(255), nullable=True),
                          Column("etag", String(255), nullable=True),
                          Column("date_created", DateTime(timezone=False), nullable=True,
                                 default=datetime.utcnow()),
                          mysql_engine="InnoDB")
            Index("site_id_idx", table.c.site_id)
            Index("user_id_idx", table.c.user_id)
            Index("country_code_idx", table.c.country_code)
            Index("ip_idx", table.c.ip)
            Index("referer_domain_idx", table.c.referer_domain)
            Index("etag_idx", table.c.etag)
            Index("date_created_idx", table.c.date_created.desc())
            table.create(checkfirst=True)
        return table

    @staticmethod
    def get_pageviews_table():
        current_date = datetime.utcnow().strftime("%Y_%m_%d")
        table_name = "page_views_{0}".format(current_date)
        try:
            table = Table(table_name, MetaData(bind=MySqlFactory.impospace_server), autoload=True)
        except Exception:
            table = Table(table_name, MetaData(bind=MySqlFactory.impospace_server),
                          Column("id", Integer, primary_key=True),
                          Column("site_id", String(255), nullable=True),
                          Column("page_view_id", String(255), nullable=True),
                          Column("sub_id", String(255), nullable=True),
                          Column("user_id", String(255), nullable=True),
                          Column("adblock_enabled", Integer, nullable=True),
                          Column("country_code", String(255), nullable=True),
                          Column("ip", String(255), nullable=True),
                          Column("domain", String(255), nullable=True),
                          Column("url", Text(), nullable=True),
                          Column("referer", Text(), nullable=True),
                          Column("user_agent", Text(), nullable=True),
                          Column("date_created", DateTime(timezone=False), nullable=True,
                                 default=datetime.utcnow()),
                          mysql_engine="InnoDB")
            Index("adblock_enabled_idx", table.c.adblock_enabled)
            Index("page_view_id_idx", table.c.page_view_id)
            Index("site_id_idx", table.c.site_id)
            Index("user_id_idx", table.c.user_id)
            Index("country_code_idx", table.c.country_code)
            Index("ip_idx", table.c.ip)
            Index("domain_idx", table.c.domain)
            Index("date_created_idx", table.c.date_created.desc())
            table.create(checkfirst=True)
        return table

    @staticmethod
    def get_impressions_table():
        current_date = datetime.utcnow().strftime("%Y_%m_%d")
        table_name = "imps_{0}".format(current_date)
        try:
            table = Table(table_name, MetaData(bind=MySqlFactory.impospace_server), autoload=True)
        except Exception:
            table = Table(table_name, MetaData(bind=MySqlFactory.impospace_server),
                          Column("id", Integer, primary_key=True),
                          Column("site_id", String(255), nullable=True),
                          Column("sub_id", String(255), nullable=True),
                          Column("user_id", String(255), nullable=True),
                          Column("creative_url", String(255), nullable=True),
                          Column("click_url", Text(), nullable=True),
                          Column("country_code", String(255), nullable=True),
                          Column("ip", String(255), nullable=True),
                          Column("user_agent", Text(), nullable=True),
                          Column("page_view_id", String(255), nullable=True),
                          Column("imp_id", String(255), nullable=True),
                          Column("type", String(255), nullable=True),
                          Column("referer_domain", String(255), nullable=True),
                          Column("referer", Text(), nullable=True),
                          Column("advertiser_name", String(255), nullable=True),
                          Column("size", String(255), nullable=True),
                          Column("date_created", DateTime(timezone=False), nullable=True,
                                 default=datetime.utcnow()),
                          mysql_engine="InnoDB")
            Index("site_id_idx", table.c.site_id)
            Index("sub_id_idx", table.c.sub_id)
            Index("user_id_idx", table.c.user_id)
            Index("creative_url_idx", table.c.creative_url)
            Index("country_code_idx", table.c.country_code)
            Index("ip_idx", table.c.ip)
            Index("page_view_id_idx", table.c.page_view_id)
            Index("imp_id_idx", table.c.imp_id)
            Index("type_idx", table.c.type)
            Index("referer_domain_idx", table.c.referer_domain)
            Index("advertiser_name_idx", table.c.advertiser_name)
            Index("size_idx", table.c.size)
            Index("date_created_idx", table.c.date_created.desc())
            table.create(checkfirst=True)
        return table

    @staticmethod
    def get_clicks_table():
        table_name = "clicks"
        try:
            table = Table(table_name, MetaData(bind=MySqlFactory.impospace_server), autoload=True)
        except Exception:
            table = Table(table_name, MetaData(bind=MySqlFactory.impospace_server),
                          Column("id", Integer, primary_key=True),
                          Column("country_code", String(255), nullable=True),
                          Column("imp_id", String(255), nullable=True),
                          Column("page_view_id", String(255), nullable=True),
                          Column("ip", String(255), nullable=True),
                          Column("referer", Text(), nullable=True),
                          Column("referer_domain", String(255), nullable=True),
                          Column("user_agent", Text(), nullable=True),
                          Column("date_created", DateTime(timezone=False), nullable=True,
                                 default=datetime.utcnow()),
                          mysql_engine="InnoDB")
            Index("country_code_idx", table.c.country_code)
            Index("imp_id_idx", table.c.imp_id)
            Index("page_view_id_idx", table.c.page_view_id)
            Index("ip_idx", table.c.ip)
            Index("referer_domain_idx", table.c.referer_domain)
            Index("date_created_idx", table.c.date_created.desc())
            table.create(checkfirst=True)
        return table

    @staticmethod
    def get_media_table():
        table_name = "media"
        try:
            table = Table(table_name, MetaData(bind=MySqlFactory.impospace_server), autoload=True)
        except Exception:
            table = Table(table_name, MetaData(bind=MySqlFactory.impospace_server),
                          Column("id", Integer, primary_key=True),
                          Column("width", Integer, nullable=True),
                          Column("height", Integer, nullable=True),
                          Column("advertiser_name", String(255), nullable=True),
                          Column("offer_name", String(255), nullable=True),
                          Column("image_id", String(255), nullable=True),
                          Column("format", String(255), nullable=True),
                          Column("image", BLOB, nullable=True),
                          mysql_engine="InnoDB")
            table.create(checkfirst=True)
            Index("height_idx", table.c.height)
            Index("width_idx", table.c.width)
            Index("advertiser_name_idx", table.c.advertiser_name)
            Index("offer_name_idx", table.c.offer_name)
            Index("image_id_idx", table.c.image_id)
            Index("format_id_idx", table.c.format)
        return table