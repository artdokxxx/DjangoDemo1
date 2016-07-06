from django.core.management.base import BaseCommand, CommandError
from AboutMeApp.models import Work,Study,Hobby,UserInfo, Organization
from datetime import date


class Command(BaseCommand):
        help = "Fill DB test data"

        def handle(self, *args, **options):
            fixtures = [
                 {
                    'object': Organization,
                    'data': [
                        {
                            'name': 'ООО "ИСС Дистрибьюшн"',
                            'site': 'http://eset.ru/',
                            'place': 'г.Москва',
                            'phone': '+7 (499) 345-67-84'
                        },
                        {
                            'name': 'ЗАО "Связной Логистика"',
                            'site': 'http://www.svyaznoy.ru/', 'place': 'г.Екатеринбург',
                            'phone': '+7 (499) 001-67-82'
                        },
                        {
                            'name': 'ООО "Рамблер"',
                            'site': 'https://rambler-co.ru', 'place': 'г.Барнаул',
                            'phone': '+7 (499) 345-67-84',
                        },
                        {
                            'name': 'ООО "Тест 4"',
                            'site': 'https://test.com', 'place': 'г.Калининград',
                            'phone': '+7 (499) 345-67-84',
                        },
                        {
                            'name': 'ООО "Тест 5"',
                            'site': 'https://example.ru', 'place': 'г.Сочи',
                            'phone': '+7 (499) 345-67-84'
                        }
                    ]
                },
                {
                    'object': Work,
                    'data': [
                        {
                            "name": 'ООО "ИСС Дистрибьюшн"',
                            "position": "Team Lead",
                            "desc": """Российское представительство ESET(ООО ИСС Дистрибьюшн) открылось в январе 2005 года и входит в тройку стратегически важных представительств компании в мире. Российское представительство ESET также курирует продвижение и продажу программного обеспечения ESET в странах СНГ. На сегодняшний день региональные офисы компании открыты в Москве, Санкт-Петербурге, Самаре, Екатеринбурге, Краснодаре, Новосибирске и Алматы со штатом более 100 человек. По данным исследовательских компаний КОМКОН и «Ромир», ESET NOD32 является вторым по популярности антивирусным решением в России и защищает каждый третий компьютер. При этом 90% пользователей рекомендуют продукты ESET NOD32 своим друзьям и знакомым.""",
                            "date_start": "2011-3-1",
                            "date_finish": "2013-4-1",
                            "logo": "eset_logo.png"
                        },
                        {
                            "name": 'ЗАО "Связной Логистика"',
                            "position": "Team Lead",
                            "desc": "Связной» — российская компания, федеральная розничная сеть, специализирующаяся на продаже услуг сотовых операторов и провайдеров проводного доступа в интернет, персональных средств связи, аксессуаров, портативной цифровой аудио- и фототехники.",
                            "date_start": "2013-4-1",
                            "date_finish": "2013-11-1",
                            "logo": "svz_logo.png"
                        },
                        {
                            "name": 'ООО "Рамблер"',
                            "position": "Head of IT Department",
                            "desc": "Rambler&Co — одна из крупнейших российских групп компаний, работающих в области медиа, технологий и электронной коммерц",
                            "date_start": "2013-11-1",
                            "date_finish": None,
                            "logo": "rambler_logo.png"
                        }, {"name": 'ООО "Тест 4"',
                            "position": "Team Lead",
                            "desc": """выаываываыв""",
                            "date_start": "2011-3-1",
                            "date_finish": "2013-4-1",
                            "logo": "eset_logo.png"},
                        {"name": 'ООО "Тест 5"',
                            "position": "Team Lead",
                            "desc": """впвыывп""",
                            "date_start": "2011-3-1",
                            "date_finish": "2013-4-1",
                            "logo": "eset_logo.png"},
                    ]
                },
                {
                    'object': Hobby,
                    'data': [{"name": "Программирование", "ico_fa": "code"},
                        {"name": "Велоспорт", "ico_fa": "bicycle"},
                        {"name": "Авто", "ico_fa": "car"}
                    ]
                },
                {
                    'object': Study,
                    'data': [
                        {
                            "name": "(МГУПП) Московский государственный университет пищевых производств Министерства образования Российской Федерации",
                            "site": "http://www.mgupp.ru/",
                            "faculty": "Институт информационных технологий, автоматизированных систем и технологического оборудования",
                            "specialty": "230100: Информатика и вычислительная техника",
                            "degree": "Высшее (бакалавр), Дневная/Очная форма обучения.",
                            "date_start": "2008-9-1",
                            "date_finish": "2012-7-20",
                            "logo": "mgupp_logo.png"
                        },
                        {
                            "name": "(МГУПП) Московский государственный университет пищевых производств Министерства образования Российской Федерации",
                            "site": "http://www.mgupp.ru/",
                            "faculty": "Институт информационных технологий, автоматизированных систем и технологического оборудования",
                            "specialty": "230100: Информатика и вычислительная техника",
                            "degree": "Высшее (магистр), Дневная/Очная форма обучения.",
                            "date_start": "2012-9-1",
                            "date_finish": "2014-7-20",
                            "logo": "mgupp_logo.png"
                        }
                    ]
                },
                {
                    'object': UserInfo,
                    'data': [
                        {"date_birthday": "1991-1-3",
                            "first_name": "Артём",
                            "last_name": "Леонтьев",
                            "second_name": "Пупырышкин",
                            "place_birthday": "г.Сыктывкар",
                        }
                    ]
                }
            ]

            for fixture in fixtures:
                if 'object' in fixture and 'data' in fixture:
                    for rec in fixture['data']:
                        if type(rec) is dict:
                            try:
                                if fixture['object'] is Work:
                                    rec['organization'] = Organization.objects.get(name=rec['name'])
                                    del rec['name']

                                el = fixture['object'](**rec)
                                el.save()
                            except Exception as e:
                                print(e, fixture['object'])
                                continue

                            if fixture['object'] is UserInfo:
                                el.hobbies.add(1, 2, 3)