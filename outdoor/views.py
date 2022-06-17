from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Subproduct, Portfolio, Call
from django.utils import timezone
import os
products_all = Product.objects.all()
subproduct_all = Subproduct.objects.all()




def index(request):
    if request.POST.get("contact"):
        if request.POST.get("polit") == 'on':
            call = Call(client=request.POST.get("name"), phone=request.POST.get("phone"), date=timezone.now())
            call.save()


    return render(request, 'index.html', context={ 'prod': products_all })

def products(request, id_product):
    parent = Product.objects.get(id_product=id_product)
    sub = Subproduct.objects.filter(parent=parent)

    return render(request, 'product.html', context={'subproducts': sub, 'parent': parent, 'prod': products_all, 'subprod': subproduct_all  })



def about(request):
    return render(request, 'about.html', context={ 'prod': products_all })

def portfolio(request):
    portfolio_all = Portfolio.objects.all()
    return render(request, 'portfolio.html', context={'prod': products_all, 'port': portfolio_all})


def detail(request, id_product, id_subproduct):
    if request.POST.get("contact"):
        if request.POST.get("polit") == 'on':
            call = Call(client=request.POST.get("name"), phone=request.POST.get("phone"), date=timezone.now())
            call.save()
    parent = Product.objects.get(id_product=id_product)
    sub = Subproduct.objects.get(id=id_subproduct)
    return render(request, 'product-detail.html',
                  context={'prod': products_all, 'subprod': subproduct_all, 'subproduct': sub, 'parent': parent,})

def all_products(request):

    return render(request, 'all_products.html', context={'prod': products_all, 'subprod': subproduct_all})

def price(request):
    return render(request, 'price.html', context={'prod': products_all, 'subprod': subproduct_all})

def contacts(request):
    return render(request, 'contacts.html', context={'prod': products_all, 'subprod': subproduct_all})

heroku = True


def managment(request):
    if request.method == 'POST':
        if request.POST.get("category"):
            Category.objects.all().delete()
            for c in cat:
                category = Category(id_category=c, category=cat[c])
                category.save()
        elif request.POST.get("products"):
            Subproduct.objects.all().delete()
            Product.objects.all().delete()
            for prod in product:
                name = False
                for p in product[prod]:
                    if not name:
                        product_add = Product(id_product=prod, product=p[0], prw_product=p[1])
                        product_add.save()
                        name = True
                        continue
                    subproduct_add = Subproduct(subproduct=p[0], parent=Product.objects.get(id_product=prod),
                                                prw_subproduct=p[1], name=p[2], unit=p[3], price=p[4])
                    subproduct_add.save()
        elif request.POST.get("portfolio"):
            Portfolio.objects.all().delete()
            for file in os.listdir('static/portfolio'):
                print(file)
                port = Portfolio(picture='static/portfolio/'+file, text='--')
                port.save()

    return render(request, 'managment.html')


cat = {'about': 'О КОМПАНИИ',
      'products': 'ПРОДУКЦИЯ',
      'blog': 'СТАТЬИ',
      'price': 'ПРАЙС',
      'portfolio': 'ПОРТФОЛИО',
      'contacts': 'КОНТАКТЫ'
      }

product = {
    'letter': [['Объемные буквы', 'static/product/letter.jpg'],
              ['Несветовые буквы', 'static/subproduct/letter_non.jpg', 'Несветовые буквы', 'см', '60'],
              ['Объемные световые буквы', 'static/subproduct/letter_light.jpg', 'Объемные световые буквы' , 'см', '90'],
                ['Объемные буквы со световым бортом', 'static/subproduct/letter_side.jpg', 'Объемные буквы со световым бортом', 'см', '90'],
                ['Объемные буквы с контражурной подсветкой', 'static/subproduct/letter_contr.jpg', 'Объемные буквы с контражурной подсветкой', 'см', '120'],
                ['Объемные буквы с комбинированной подсветкой', 'static/subproduct/letter_combi.jpg', 'Объемные буквы с комбинированной подсветкой', 'см', '110'],
                ['Объемные буквы на подложке', 'static/subproduct/letter_base.jpg', 'Объемные буквы на подложке', 'см', '130'],
                ['Объемные буквы из пенопласта', 'static/subproduct/letter_foam.jpg', 'Объемные буквы из пенопласта','см', '70'],
                ['Объемные буквы из дерева', 'static/subproduct/letter_wood.jpg', 'Объемные буквы из дерева', 'см', '50'],
                ['Объемные буквы из нержавеющей стали', 'static/subproduct/letter_steel.jpg', 'Объемные буквы из нержавеющей стали', 'см', '100'],
                ['Объемные буквы из ПВХ', 'static/subproduct/letter_pvh.jpg', 'Объемные буквы из ПВХ', 'см', '70'],
                ['Объемные буквы из акрила', 'static/subproduct/letter_acril.jpg', 'Объемные буквы из акрила', 'см', '90'],
              ],
    'box':  [['Световые короба', 'static/product/box.jpg'],
             ['Из алюминиевого профиля', 'static/subproduct/box_alum.jpg','Световые короба из алюминиевого профиля', 'м2', '8500'],
             ['Из пластикового профиля', 'static/subproduct/box_plastic.jpg', 'Световые короба из пластикового профиля', 'м2', '8000'],
            ['Из акрила / оргстекла', 'static/subproduct/box_acryl.jpg', 'Световые короба из акрила / оргстекла', 'м2', '12000'],
            ['Из поликарбоната', 'static/subproduct/box_polycarb.jpg', 'Световые короба из поликарбоната', 'м2', '8000'],
            ['С баннерной тканью', 'static/subproduct/box_banner.jpg', 'Световые короба с баннерной тканью','м2', '10000'],
            ['Со сменным изображением', 'static/subproduct/box_change.jpg', 'Световые короба со сменным изображением','м2', '8000'],
            ['Фигурные', 'static/subproduct/box_shape.jpg', 'Световые короба фигурные', 'м2', '13000'],
            ['С инкрустацией', 'static/subproduct/box_in.jpg', 'Световые короба с инкрустацией', 'м2', '14000'],
            ['Из композита', 'static/subproduct/box_composite.jpg', 'Световые короба из композита', 'м2', '12500'],
            ['Нестандартные', 'static/subproduct/box_nonstandart.jpg', 'Световые короба нестандартные','м2', '13000'],
    ],
    'console': [['Кронштейны, консоли', 'static/product/console.jpg'],
                ['Односторонние панель-кронштейны', 'static/subproduct/console_1side.jpg', 'Односторонние панель-кронштейны','шт', '6000'],
                ['Двухсторонние панель-кронштейны', 'static/subproduct/console_2side.jpg', 'Двухсторонние панель-кронштейны', 'шт', '8500'],
                ['Прямоугольные, квадратные панель-кронштейны', 'static/subproduct/console_square.jpg', 'Прямоугольные, квадратные панель-кронштейны', 'шт', '8500'],
                ['Круглые/овальные панель-кронштейны', 'static/subproduct/console_round.jpg', 'Круглые/овальные панель-кронштейны', 'шт', '8500'],
                ['Панель-кронштейны с инкрустацией', 'static/subproduct/console_in.jpg', 'Панель-кронштейны с инкрустацией', 'шт', '12000'],
                ['Фигурные панель-кронштейны', 'static/subproduct/console_shape.jpg', 'Фигурные панель-кронштейны', 'шт', '9000'],
                ['Нестандартные панель-кронштейны', 'static/subproduct/console_nonstandart.jpg', 'Нестандартные панель-кронштейны', 'шт', '10000'],

    ],
    'panel': [['Световые панели', 'static/product/panel.jpg'],
              ['Кристалайты', 'static/subproduct/panel_crystal.jpg', 'Кристалайты','шт', '5000'],
              ['Фреймлайты', 'static/subproduct/panel_framelight.jpg', 'Фреймлайты', 'шт', '3000'],
              ['Магнетики односторонние', 'static/subproduct/panel_1magnetic.jpg', 'Магнетики односторонние', 'шт', '4000'],
              ['Магнетики двухсторонние', 'static/subproduct/panel_2magnetic.jpg', 'Магнетики двухсторонние', 'шт', '6000'],
              ['Настенные световые панели', 'static/subproduct/panel_wall.jpg', 'Настенные световые панели', 'шт', '5000'],
              ['Подвесные световые панели', 'static/subproduct/panel_pendant.jpg', 'Подвесные световые панели', 'шт', '5500'],
              ['Настольные световые панели', 'static/subproduct/panel_table.jpg', 'Настольные световые панели','шт', '6000'],
              ['Уличные световые панели', 'static/subproduct/panel_outdoor.jpg', 'Уличные световые панели','шт', '12000'],

    ],
    'trade': [['Торговое оборудование', 'static/product/trade.jpg'],
              ['Ресепшены', 'static/subproduct/trade_reception.jpg', 'Ресепшены', 'шт', '0'],
              ['Стелажи для аксесуаров', 'static/subproduct/trade_stelage.jpg', 'Стелажи для аксесуаров', 'шт', '0'],
              ['Тумбы', 'static/subproduct/trade_cabinet.jpg', 'Тумбы', 'шт', '0'],
              ['Гондоллы', 'static/subproduct/trade_gondolla.jpg', 'Гондоллы', 'шт', '0'],
              ['Столы обслуживания клиентов', 'static/subproduct/trade_manage.jpg', 'Столы обслуживания клиентов', 'шт', '0'],
              ['Стойки для образцов', 'static/subproduct/trade_stend.jpg', 'Стойки для образцов', 'шт', '0'],
              ['Кассы', 'static/subproduct/trade_kassa.jpg', 'Кассы', 'шт', '0'],
               ['Композиции', 'static/subproduct/trade_composition.jpg', 'Композиции', 'шт', '0'],
               ['Мебель из ЛДСП', 'static/subproduct/trade_furniture.jpg', 'Мебель из ЛДСП', 'шт', '0'],
               ['Подставки', 'static/subproduct/trade_acryl.jpg', 'Подставки', 'шт', '0'],
               ['Корзины', 'static/subproduct/trade_basket.jpg', 'Корзины', 'шт', '0'],
               ['Торговая мебель', 'static/subproduct/trade_trade.jpg', 'Торговая мебель', 'шт', '0'],
               ['Примерочные', 'static/subproduct/trade_dress.jpg', 'Примерочные', 'шт', '0'],
               ['Мебель из МДФ', 'static/subproduct/trade_mdf.jpg', 'Мебель из МДФ', 'шт', '0'],
               ['Стелажи с подсветкой', 'static/subproduct/trade_light.jpg', 'Стелажи с подсветкой',  'шт', '0'],
               ['Рекламно-информационные стенды', 'static/subproduct/trade_st.jpg', 'Рекламно-информационные стенды', 'шт', '0'],
               ['Острова', 'static/subproduct/trade_island.jpg', 'Острова','шт', '0' ],
               ['Рекламно-информационные стойки', 'static/subproduct/trade_shtender.jpg', 'Рекламно-информационные стойки', 'шт', '0'],
               ['Встраиваемые стелажи', 'static/subproduct/trade_in.jpg', 'Встраиваемые стелажи', 'шт', '0'],
               ['Стойки со встраиваемой техникой', 'static/subproduct/trade_on.jpg', 'Стойки со встраиваемой техникой', 'шт', '0'],
    ],
    'sign': [ ['Таблички', 'static/product/sign.jpg'],
              ['Из оргстекла', 'static/subproduct/sign_acryl.jpg', 'Таблички из оргстекла', 'шт', '500'],
              ['Из ПВХ', 'static/subproduct/sign_pvh.jpg', 'Таблички из ПВХ', 'шт', '300'],
              ['Из дерева', 'static/subproduct/sign_wood.jpg', 'Таблички из дерева', 'шт', '1000'],
              ['Из металла', 'static/subproduct/sign_metal.jpg', 'Таблички из металла', 'шт', '2000'],
              ['Из нержавеющей стали', 'static/subproduct/sign_steel.jpg', 'Таблички из нержавеющей стали', 'шт', '2000'],
              ['С рамками', 'static/subproduct/sign_frame.jpg', 'Таблички с рамками', 'шт', '800'],
              ['Объемные', 'static/subproduct/sign_volume.jpg', 'Таблички объемные', 'шт', '1000'],
              ['Номерки', 'static/subproduct/sign_number.jpg', 'Номерки', 'шт', '200'],
              ['С подсветкой', 'static/subproduct/sign_light.jpg', 'Таблички с подсветкой', 'м2', '12000'],
              ['Указатели', 'static/subproduct/sign_sign.jpg', 'Указатели', 'шт', '500'],
    ],
    'construction': [['Конструкции', 'static/product/const.jpg'],
                      ['Крышные установки', 'static/subproduct/constr_letter.jpg', 'Крышные установки', 'шт', '0'],
                      ['Стеллы', 'static/subproduct/constr_stella.jpg', 'Стеллы', 'шт', '0'],
                      ['Пилоны', 'static/subproduct/constr_pilon.jpg', 'Пилоны',  'шт', '0' ],
                      ['Входные группы', 'static/subproduct/constr_entrance.jpg', 'Входные группы',  'шт', '0'],
    ],
    'stend': [ ['Информационные стенды', 'static/product/stend.jpg'],
               ['Настенные', 'static/subproduct/stend_wall.jpg', 'Информационные стенды настенные',  'шт', '850'],
               ['Напольные', 'static/subproduct/stend_floor.jpg', 'Информационные стенды напольные',  'шт', '1500'],
               ['Уличные', 'static/subproduct/stend_street.jpg','Информационные стенды уличные',  'шт', '0'],
    ],
    'board': [ ['Доски почета', 'static/product/board.jpg'],
               ['Настенные доски почета', 'static/subproduct/board_wall.jpg', 'Настенные доски почета',  'шт', '800'],
               ['Напольные доски почета', 'static/subproduct/board_floor.jpg', 'Напольные доски почета',  'шт', '1500'],
               ['Уличные доски почета', 'static/subproduct/board_street.jpg', 'Уличные доски почета',  'шт', '0'],
    ],
    'rollup': [ ['Рекламные стенды', 'static/product/rollup.jpg'],
                ['Ролл ап (Roll up) стенды', 'static/subproduct/rollup.jpg', 'Ролл ап (Roll up) стенды',  'шт', '0'],
                ['Напольные баннерные стенды', 'static/subproduct/rollup_x.jpg', 'Напольные баннерные стенды',  'шт', '0'],
                ['Pop Up стенды', 'static/subproduct/rollup_popup.jpg', 'Pop Up стенды',  'шт', '0'],
                ['Fold Up стенды', 'static/subproduct/rollup_foldup.jpg', 'Fold Up стенды',  'шт', '0'],
                ['Пресс волл - Мобильные стенды', 'static/subproduct/rollup_presswall.jpg', 'Пресс волл - Мобильные стенды',  'шт', '0'],
                ['Рекламные промо стойки', 'static/subproduct/rollup_promo.jpg', 'Рекламные промо стойки',  'шт', '0'],
                ['Напольные, настольные и настенные буклетницы', 'static/subproduct/rollup_foor.jpg', 'Напольные, настольные и настенные буклетницы',  'шт', '0'],
                ['Тантамарески', 'static/subproduct/rollup_tamtama.jpg', 'Тантамарески',  'шт', '0'],
                ['Штендеры', 'static/subproduct/rollup_shtender.jpg', 'Штендеры',  'шт', '0'],
]

}