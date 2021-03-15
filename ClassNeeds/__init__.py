#coding:utf-8
from flask import Flask, render_template, request, redirect, url_for, session, make_response
from lxml import etree
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = "C:\Program Files (x86)\chromedriver.exe"

import json
import yagmail
# from urllib.request import urlopen
import pdfkit
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'superkey'

arr = [
"77392a78-8326-4ef4-b247-be7d1130a5b1",
"8773a853-ec8b-4602-9264-8a4692fc25a0",	
"dec30d5c-98b2-416f-b667-90b727c22b48",	
"d59d03c3-16db-4711-8318-9613b1a2463c",	
"69feed61-6929-4ce4-90e2-352e411ffa49",	
"ad0176a9-38ee-4e52-98dd-fccbda98c767",	
"9af49bbf-78b7-45dd-9d1f-452ca62bf63a",	
"57b3c9b1-116a-4ad7-bd06-3f5a437bcb2d",	
"a401046b-899d-400e-8c1a-7e7aedc735b5",	
"ebead779-22b0-412d-bc3c-d5e802b09dfb",
"5fce853f-58d1-4d88-8029-3cad48f1abc2",
"1938573b-55be-4274-a2b0-9e20451f8ba6",
"3058080c-8708-44c6-8050-33dc8c9e247c",
"907a43ea-3cff-444c-9141-49198fadee85",
"7542df7b-72cd-476a-9863-a57a0158d9b5",
"f9101369-86a2-4260-8054-00a577dbb87b",
"041891ec-b764-4f45-95b5-e3f1f7c177a0",
"1ffde9bd-f4c3-496e-95bf-cf460f7c5869",
"9c9b63fd-94d1-4144-8fcc-a6ef668c1a4d",
"1e57e671-5388-403e-9298-89a5a50d1911",
"2E7E16C2-8769-4D9E-BBFF-D5492A6E5592",
"1D7FB452-A0D5-498A-915C-0FB3515AE8AE",
"BBD8CDAB-8435-4594-B02E-32EA09241328",
"75A152FC-7A71-4BEC-9D6B-54BAD2B11979",
"E3D75C34-95BF-4735-999E-4E865987DF57",
"D769A05D-9249-41A4-A9A1-36573561ACA7",
"99EB5D7C-FA22-4CD8-953D-E41B2ADA8E54",
"9D54D9C5-7008-4A6C-8BE9-3BFC3BEF9DFD",
"D03EDC26-2D53-45E1-9491-258DF2FBBD62",
"185C8AAC-F7A0-46B3-BB5E-E642FD9E9E47",
"916D8DE3-5520-43FA-8F68-FA09244C6132",
"251FABB2-6EA4-4357-95DD-32163E08D4B7",
"FA4E8CDD-2085-414C-8BC6-CB44AE849895",
"A12646E2-5DE9-4407-A54D-58A312240512",
"D151475F-FBCA-4267-B4AE-33C9A675C093",
"13ED5199-52A8-408D-ABF5-EE5EA6693411",
"D4DD6945-B9AE-4F5E-A4AB-05D1BB9E8130",
"7DC8446B-4C9D-4472-BD50-BC9DF952BF64",
"3E2FE8F9-7FC8-435D-BC6E-F6F8C662438C",
"E6ACB89D-FE03-4867-AD23-FECBDF310C45",
"973F2DEA-DDB4-4AA3-A7A1-34C9FB9CD82E",
"14CAE04A-B103-4DF1-BAAB-DD68C1EBFE15",
"ABDF31D2-4E01-4F20-802F-8F443F7D9FE2",
"6F39E804-8A2F-493E-BCD3-B1F6882F9198",
"EBC1ADCF-7A7C-43D1-84F8-0B38B4034198",
"93089E2E-2866-4ED9-B2D5-8D18384C7AF1",
"F4AA4477-2ACB-44CB-A513-D72EC1C5E23F",
"C13D1B58-BD49-46D5-9043-C9F0EEC09BFF",
"0DB38043-95D4-4CB5-A76E-4B85BBA9CAD9",
"5EDE7616-06FD-4842-BA85-088B2B695DB5",
"65255918-17AB-4584-9730-3A126680A61C",
"2A4285E5-C0B1-4608-AD92-23BE85A329F1",
"599569AA-1678-4DA3-85A4-6CC8E9389BB3",
"05EF11D2-663A-4CB1-A495-EDB6AD2444A2",
"7CA5D0A9-5A7A-475A-A8C2-8A7BC879E8E0",
"0AE07329-8B1A-4C66-AE6A-69A9B332CB2D",
"D7358D4E-9810-49E0-AD64-98D69613B5FC",
"A5A7E8BF-39C8-4B79-815A-6C12DEA7750E",
"A9DCBC66-8775-435E-8156-75BA2D5B74B7",
"63CB97D8-4AC2-4EFB-AC1B-5764D9D737C2",
"19E4C777-5258-49FE-A6B9-BA2F16CD1135",
"61615A59-B2A9-4B4B-BED8-E06AC1D8FC3D",
"020740F0-1CDB-4FAE-A29E-500C47A39D0D",
"4B5A87A6-545E-49D4-B597-F4801320AB33",
"CF11866A-FE24-42AF-9F9B-E948C6C5C5B0",
"B4647E9B-C046-43D2-9503-CA0BB47826D6",
"F32C23AC-8CAF-45CA-9522-45BBDB2A3FDE",
"80A6CD1A-D526-41DA-B32D-99EA53AEBF2B",
"D543AF27-ECA8-4798-B919-A660F571D6FC",
"3B26DE8F-917E-4630-A583-B87306B5A479",
"10F523F8-DB30-44F6-9AB2-362FE8CA7D45",
"320CDE3C-6AB8-4A73-BE0F-7F717E8FCBEA",
"BA26D4AD-BB41-4541-8615-F9A7AB41E80F",
"1E632564-E85B-4220-A050-DAEE982C030E",
"357C1F26-DDC0-465B-B004-770AA6080A9B",
"2F9FEE96-ADBE-4A7A-AA3A-77A83E13BDA3",
"28BBEDF7-6F7E-40AF-AF68-F382AE5A8584",
"C7E69611-EB80-463A-9255-0AD2DE6C82FE",
"2CA42466-33C4-4D78-9183-312236DB4649",
"D1A02364-5FCC-44F1-8D30-CC1CED9CBCB6",
"1F00BCDC-42A3-434E-AFA6-F6FAD7ED25AF",
"0309464E-0DA5-465F-842C-A30BC1A86330",
"DA28DE6A-9485-465B-8134-BA14E5D83D25",
"EE843267-3F7D-4E38-9914-952E35C32A6C",
"FD62D843-8463-4DA3-B600-208121E0A6B9",
"76FABD66-1BF7-4435-9DCD-D35132E87ABB",
"BB92A3D5-332E-4B6A-9DF5-B7A252FE5AE9",
"E8542159-E9FD-4212-AED2-C275AF7049CC",
"79B77743-B039-4967-B5A2-4980EBA549B7",
"E26C7580-3916-41EE-B643-3010862CE868",
"A69990F5-887F-4E9F-B849-0E19FA3FCB47",
"D0527303-5A11-4B69-8204-318406438ECF",
"F5C17519-BED9-4854-B392-2BCEBAB5DF3C",
"B96E6F40-0D9E-44E8-8D42-3B8D737B023A",
"E33C6B4E-7CED-49BF-A194-F77819AA226C",
"17D30F1B-8D16-4E83-8D9A-A064691535FE",
"D2B43CF8-1961-46D1-8D77-FE1C726CE596",
"E58E39CE-81F2-417F-B680-3E857BECE717",
"D746032C-45BC-4C3F-956E-A8F43E9B109B",
"1D9D0100-26F3-448E-B3A2-D35517554321",
"F765DD09-418D-492C-BF9F-F82AB32557C0",
"9C50A7D7-3140-4441-B927-DB6A9DD2F80F",
"8F8AEE8C-B876-4D24-99CE-DA40D882AAEB",
"25BF341E-CE93-4806-A8D1-47E0F3DAB8F2",
"A5104AB2-6650-4B36-9D66-670C87EB46B6",
"C454E605-4197-4364-8DF8-AE2B6D55B0D3",
"FA90608B-D90E-4DF3-A781-85B2DE8E0B22",
"77EE1372-AE00-479B-9D60-25E0BC99DC77",
"5AE95CED-DDD7-44B8-847A-096523D2DF1E",
"83122903-987C-4100-B1FF-A364D29936B9",
"DDE27101-C893-40B5-A57F-F08BA886E266",
"6165BE72-0B9E-41CF-AAA2-3DA093C788EB",
"D12702D6-EC8D-43CA-B2FD-44B601FB28FE",
"557B10F2-B852-4A7D-9E70-8D7AC1EE176C",
"A445B3A7-4220-47E9-84D0-92DFAAB65CCB",
"582977BE-DD22-42F6-8AC0-8552E9953BA6",
"A9AACFCD-E8B8-4E6D-9CBD-2A52325005D3",
"BD2162F5-7556-4063-ACA4-4CBD17CF33E1",
"FD430EF4-C954-4E18-967E-CB6E3A12C621",
"8BD48ADE-8548-4BE5-80BE-0130577594BC"
]


i = 0
cha = arr[i]

yag = yagmail.SMTP(user="pc576063015@gmail.com",password="kcqhxevrfggvbrlo",host ='smtp.gmail.com')



@app.route('/<string:key>', methods =['GET','POST'])
def classNeeds(key):

    global cha, i, arr

    if key == cha:
       

        # response = make_response(pdf)
        # response.headers['Content-Type'] = 'application/pdf'
        # response.headers['Content-Disposition'] = \
        #     'inline; filename=%s.pdf' % 'yourfilename'
        # return response

        #打印成pdf binary文件储存
        # pdfkit.from_url("https://www.chegg.com/homework-help/assume-length-typical-televised-baseball-game-including-comm-chapter-5-problem-8P-solution-9781111529055-exc#", "out.pdf", configuration=config, options=options)
        #---------
        # pdf = pdfkit.from_url('https://www.chegg.com/homework-help/assume-length-typical-televised-baseball-game-including-comm-chapter-5-problem-8P-solution-9781111529055-exc#', 'False', configuration=config, options=options)
        # response = make_response(pdf)
        # response.headers['Content-Type'] = 'application/pdf'
        # response.headers['Content-Disposition'] = \
        #     'inline; filename=%s.pdf' % 'yourfilename'
        # return response
        #----------
        #------------------








        if request.method == 'POST':
            print("if = post:", i)
            url = request.form.get('url')
            email = request.form.get('email')
            i = i+1
            cha = arr[i]

            # answer_list = info(url)
            info(url)

            print('done')

        #     if not email:

        #         # return render_template('check.html', links=answer_list)
        #         return render_template('check.html')

        #     else:
        #         try:
        #             contents = answer_list
        #             yag.send(email,'subject',contents)
        #         except:
        #             pass
        #         finally:
        #             return render_template('check.html', links=answer_list)
        # else:
        #     return render_template('index.html')
    return render_template('index.html')

    

#spider


def info(input_url):
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/json,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1",
    "Cookies": "_fbp=fb.1.1599551930472.961746718;user_geo_location=%7B%22country_iso_code%22%3A%22US%22%2C%22country_name%22%3A%22United+States%22%2C%22region%22%3A%22CA%22%2C%22region_full%22%3A%22California%22%2C%22city_name%22%3A%22Redwood+City%22%2C%22postal_code%22%3A%2294061%22%2C%22locale%22%3A%7B%22localeCode%22%3A%5B%22en-US%22%5D%7D%7D; C=0; O=0; V=4356274cc0991fb91b6340017e8448e15f5739b9b02673.21839414; AMCVS_3FE7CBC1556605A77F000101%40AdobeOrg=1; s_ecid=MCMID%7C70066539318470322722142659624130644636; _pxvid=218ce439-f1a9-11ea-8114-0242ac120005; mcid=70066539318470322722142659624130644636; sbm_sbm_id=0100007FBA39575F390004740271C934; sbm_dma=807; sbm_country=US; sbm_mcid=70066539318470322722142659624130644636; _cs_c=1; _rdt_uuid=1599551932021.f1003cec-93f0-4392-a24c-3d53da4f0282; _ga=GA1.2.1201949820.1599551932; _gcl_au=1.1.53151011.1599551932; aam_tnt=aam%3D2053348; LPVID=UzMzk3MjUxYTYzNzNiZjdj; sbm_gaid=1201949820.1599551932; __gads=ID=c889d609648b3b14:T=1599551939:S=ALNI_MaTstMjFhpBC-221L9Vomdpy3rkZA; U=a1d4302c6e6705518af7072e0ebd7713; optimizelyEndUserId=oeu1599551955907r0.3601443538482556; capp_promo_modal_shown=true; _sdsat_cheggUserUUID=eb2c306f-a384-4198-a7ae-1c918d3f63aa; csrftoken=pGN2MinWmb7vyZ6JohwMqHDw3N9gw5e7xumw1uA8I2SfD0a8o8qvG7JaCCcaaC6V; _scid=c96e7b3d-8f61-488f-93b9-068f8a495a7a; _sctr=1|1599548400000; _vid=w19pMgaQAhowxTZSTRVk; DFID=web|w19pMgaQAhowxTZSTRVk; _CT_RS_=Recording; WRUID=2942149550964892; aam_uuid=70038712711979504422139874905152706214; _sdsat_highestContentConfidence={%22course_uuid%22:%22bac9f6a0-58f8-435f-94c7-d75365552dda%22%2C%22course_name%22:%22financial-accounting%22%2C%22confidence%22:0.3758655737704918%2C%22year_in_school%22:%22college-year-2%22%2C%22subject%22:[{%22uuid%22:%22d8e55861-d848-4aff-adf0-69de26f0e919%22%2C%22name%22:%22accounting%22}%2C{%22uuid%22:%228de28eb7-755d-4df8-90f6-700725295632%22%2C%22name%22:%22finance%22}]}; adobeujs-optin=%7B%22aam%22%3Atrue%2C%22adcloud%22%3Atrue%2C%22aa%22%3Atrue%2C%22campaign%22%3Atrue%2C%22ecid%22%3Atrue%2C%22livefyre%22%3Atrue%2C%22target%22%3Atrue%2C%22mediaaa%22%3Atrue%7D; AMCV_3FE7CBC1556605A77F000101%40AdobeOrg=-408604571%7CMCIDTS%7C18516%7CMCMID%7C70066539318470322722142659624130644636%7CMCAAMLH-1600457592%7C9%7CMCAAMB-1600457592%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C-1513874356%7CMCOPTOUT-1599859992s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18521%7CvVersion%7C4.6.0; sbm_sbm_session_id_2=e53d04eb-f9ad-4147-823f-f90df7c174b6; aamsc=aam%3D2053348; _gid=GA1.2.1868641636.1599852795; schoolapi=07f90e85-8cbb-4640-880f-38fe0ce3fad4|0.333333333; PHPSESSID=r05pcqhgk52g3gkgbjllacp1l7; CSessionID=8cc71b68-b7a1-4312-a9a8-4eee1c27cf39; LPSID-51961742=UCkxpTpATUuEVKf5H7Mivg; id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodWIuY2hlZ2cuY29tIiwic3ViIjoiZWIyYzMwNmYtYTM4NC00MTk4LWE3YWUtMWM5MThkM2Y2M2FhIiwiYXVkIjoiQ0hHRyIsImV4cCI6MTYxNTYyMjgwNCwiaWF0IjoxNTk5ODUyODA0LCJlbWFpbCI6IjEyMjUyNjIyNDNAcXEuY29tIn0.L5hEUeZ_VDJgC1xKqj_5ray31p6Qq3kB-6PH6F4KTXPOXmVPh1LcNHjg_-hyntm6C79MjGHqY1m69PrV7X5w1iMFsJAxtIDLzfHRgm32R8d-VnqYKc1hYJQPjxZtOb6_WT0peWs7BGHChGqkQwosHzU76kjG7vfp6UNvJBLBc3ymn9K8wTHzcMG7MbFYG8W5evkrBR60vG8rSbXe6HpZux8g8MJneCKZmc3l3pznKIpEfV0jUlGxEnk_XOuU3cTZ-0KwojZzzj8pjusqo6uCxywoJtW2ewXmykiuLcWVoipX4R9vWErq4JiRf1Eqw2A93n1rtCpxOYpo4JxyEp467A; refresh_token=a9tmVJ62GnCViz4YbqKGTtTCENdtXejj; SU=FWx2NybCYr3-HCmfmKg7PltqIogPBWxL_lMfrMmOB1QOYd-iuatMgUO41Z8bHnPUJDvKy3J5U_Q7hGtvzUZTpP9o-rkmVuRnONoT7kpr8HzKzZbQ59hhq52UB75X7XtS; exp=A311C%7CA579C%7CA803B%7CC020A%7CP569C%7CP570C%7CP571C%7CA185C%7CA560B%7CA594A%7CA347B%7CA110B%7CA288C%7CA969B%7CA270C%7CA935B%7CA890H%7CA966D%7CA698A%7CA278C%7CP266E; expkey=FCF9479BC692490F7E722C8A06B3EBE0; sbm_a_b_test=3-control; BIBSESSID=8333c322-2a20-4779-aed6-86a441cc1548; userRole=mybib; _sdsat_authState=Hard%20Logged%20In; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; OptanonConsent=consentId=624197ac-323f-4452-b920-73a613ec142c&datestamp=Fri+Sep+11+2020+13%3A00%3A51+GMT-0700+(Pacific+Daylight+Time)&version=6.4.0&interactionCount=1&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=snc%3A1%2Cprf%3A1%2Cfnc%3A1%2Ctrg%3A1%2CSPD_BG%3A1&AwaitingReconsent=false; eb2c306f-a384-4198-a7ae-1c918d3f63aa_TMXCookie_60=true; _uetsid=3021dfb1dc4f0cb9584ec20beefde01f; _uetvid=e9cea5b5bf28069ae40b4b40ca14cce1; _gat=1; _cs_cvars=%7B%221%22%3A%5B%22Page%20Name%22%2C%22TBS%20Chapter%20Page%22%5D%2C%222%22%3A%5B%22Experience%22%2C%22desktop%22%5D%2C%223%22%3A%5B%22Page%20Type%22%2C%22pdp%22%5D%2C%224%22%3A%5B%22Auth%20Status%22%2C%22Hard%20Logged%20In%22%5D%7D; _cs_s=6.1; _cs_id=aba001e3-c8c6-a69a-e0a6-58bb37d08ccd.1599551932.26.1599854453.1599852488.1.1633715932282.Lax.0; __CT_Data=gpv=71&ckp=tld&dm=chegg.com&apv_79_www33=73&cpv_79_www33=73&rpv_79_www33=17; _px3=2f9a2f5eabcb1ff3ca7ba0fb0e6a3fea7692065c00a41c4292214abdcf4c595b:QoPVlAunIBu5bi65NY6HaIcwIvj3PXXjJmr6x0ZtuhOW803C5YX8BlNO14T/O5vh1wpkjrSc89ZmWdKhsBYEIg==:1000:gFjzUZa0H7bsHMP0RiMel3afZbMNKAGW3FX1ujOIeRRFPF+ePPo/XDtMwu0U2n0ePe+0t4OxJynWpeUnOOsgy84NAPPHx9/jYPsj86vIPXG/sDvphpUpUQeb2csprdlB3VVebVcCXG4jEbMR2WfQu1IRG2H+poSQv9Xd8nJqyjU=; _px=QoPVlAunIBu5bi65NY6HaIcwIvj3PXXjJmr6x0ZtuhOW803C5YX8BlNO14T/O5vh1wpkjrSc89ZmWdKhsBYEIg==:1000:IHcGb6MpJitGt8dYvsavWDJzFLRdHdqNtR0Ad19g++7xLmq0kS7xjs4UPOoY/deTF9bB/XkrmhesjAKy0CoUNTbw00XL/WHE+0OEiF6ySHNImBYIeh626wqiROQg2BTrqyA2qZ6DY3SUm9u33xX4FynQsv9futNueOADv9/AchVxqZ3qFJeC9H/M4CDYwrce2HJKa7HlVAbEYwLjo+5NvXXr5vy5zDElLCE3UoPLmNX4Aqml+ETv4rLS+ZZfQrk+0vdeKqfKVZa64CRxUZsLCA==; s_pers=%20buFirstVisit%3Dcs%252Ccore%252Chelp%7C1757492192592%3B%20gpv_v6%3Dchegg%257Cweb%257Ccs%257Ctbs%257Ctbs%2520chapter%2520page%7C1599856267340%3B; s_sess=%20buVisited%3Dcs%252Ccore%252Chelp%3B%20s_sq%3D%3B%20cheggCTALink%3Dfalse%3B%20SDID%3D438E358076727520-22BAB890F6BE4C1E%3B%20s_cc%3Dtrue%3B%20s_ptc%3D0.16%255E%255E0.00%255E%255E0.00%255E%255E0.00%255E%255E0.90%255E%255E0.02%255E%255E2.71%255E%255E0.10%255E%255E3.92%3B"
    }

    # driver = webdriver.Chrome(PATH)
    # driver.get("https://www.chegg.com/homework-help/questions-and-answers/stuck-part-b-question-done-far-part--thank-help-q34350529")
    # time.sleep(5)
    # log = driver.find_element_by_xpath("//*[@id='eggshell-14']/a")
    # log.send_keys(Keys.RETURN)
    # login_form = driver.find_element_by_id('emailForSignIn')
    # login_form.send_keys('1225262243@qq.com')
    # password = driver.find_element_by_id('passwordForSignIn')
    # password.send_keys('Llx1225262243')
    # signin = driver.find_element_by_xpath("//*[@id='eggshell-8']/form/div/div/div/footer/button")
    # signin.send_keys(Keys.RETURN)

    

    session = requests.Session()

    time.sleep(15)

    response = session.get(input_url,headers=headers)

    html = etree.HTML(response.text)
    
    time.sleep(15)

    with open('chegg3.html','w', encoding='utf-8') as fp:
        fp.write(response.text)

    # answer_url = html.xpath('//*[@id="solution-player-sdk"]/section/section/div[1]/section[1]/section/ol/li[3]/section/div/div/div/p')
    print('---')

    # answer_url = html.xpath('//*[@class="txt-body answer-body"]/div/p/img/@src')

    # return answer_url

    #--------------------------------------------------------
    # with open('chegg3.html','w', encoding='utf-8') as fp:
    #     fp.write(response.text)

    # pdfkit.from_file('chegg3.html', 'out.pdf', configuration=config)
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header' : [
            ('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0'),
            ('Accept', 'application/pdf,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
            ('Accept', 'application/json, text/javascript, */*; q=0.01'),
            ('Accept-Language', 'en-US,en;q=0.5'),
            # ('Accept-encoding', 'gzip, deflate'),
            ('DNT', '1'),
            ('Connection', 'close'),
            ('Upgrade-Insecure-Requests','1'),
            ('Content-type', 'application/pdf; charset=UTF-8')
            ],

        'cookie': [
            ('_fbp', 'fb.1.1599551930472.961746718'),
            ('user_geo_location','%7B%22country_iso_code%22%3A%22US%22%2C%22country_name%22%3A%22United+States%22%2C%22region%22%3A%22CA%22%2C%22region_full%22%3A%22California%22%2C%22city_name%22%3A%22Redwood+City%22%2C%22postal_code%22%3A%2294061%22%2C%22locale%22%3A%7B%22localeCode%22%3A%5B%22en-US%22%5D%7D%7D'),
            ('C','0'),
            ('O','0'),
            ('V', '4356274cc0991fb91b6340017e8448e15f5739b9b02673.21839414'),
            ('AMCV_3FE7CBC1556605A77F000101%40AdobeOrg','1'),
            ('s_ecid','MCMID%7C70066539318470322722142659624130644636'),
            ('_pxvid','218ce439-f1a9-11ea-8114-0242ac120005'), 
            ('_cs_c', '1'),
            ('_ga', 'GA1.2.1201949820.1599551932'),
            ('_gid', 'GA1.2.1557069136.1599551932'),
            ('_gcl_au', '1.1.53151011.1599551932'),
            ('aam_tnt','aam%3D2053348'),
            ('aam_uuid','70038712711979504422139874905152706214'),
            ('LPVID','UzMzk3MjUxYTYzNzNiZjdj'),
            ('U', 'a1d4302c6e6705518af7072e0ebd7713'),
            ('intlPaQExitIntentModal', 'hide'),
            ('optimizelyEndUserId', 'oeu1599551955907r0.3601443538482556'),
            ('capp_promo_modal_shown', 'true'),
            ('_scid','c96e7b3d-8f61-488f-93b9-068f8a495a7a'),
            ('_sctr', '1|1599548400000'),
            ('BIBSESSID','f6ff2d6e-1f14-4625-af8f-e05279d942b3'),
            ('userRole','mybib'),
            ('AMCV_3FE7CBC1556605A77F000101%40AdobeOrg','-408604571%7CMCIDTS%7C18514%7CMCMID%7C70066539318470322722142659624130644636%7CMCAAMLH-1600212397%7C9%7CMCAAMB-1600212397%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C-1513874356%7CMCOPTOUT-1599614797s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18521%7CvVersion%7C4.6.0'),
            ('exp','A311C%7CA579C%7CA803B%7CC020A%7CP569C%7CP570C%7CP571C%7CA185C%7CA560B'),
            ('LPSID-51961742','33Y8OsV4SZSGdYPD3x8uVw'),
            ('expkey','C9D60F127B2E43C12693F1A9E803CBF9'),
            ('PHPSESSID','6reh0kjuklj39hmttgnk4uv820'),
            ('CSessionID', '82c8c4a1-d6aa-4420-a2ba-5e905d297159'),
            ('aamsc','aam%3D2053348'),
            ('_gat','1'),
            ('WRIgnore', 'true'),
            ('_gali', 'eggshell-15'),
            ('OptanonConsent','consentId=624197ac-323f-4452-b920-73a613ec142c&datestamp=Tue+Sep+08+2020+01%3A01%3A36+GMT-0700+(Pacific+Daylight+Time)&version=6.4.0&interactionCount=1&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=fnc%3A1%2Csnc%3A1%2Cprf%3A1%2Ctrg%3A1%2CSPD_BG%3A1&AwaitingReconsent=false'),
            ('_px3','8cb743f84dab26bb2dd2f5c409f2f399ca3967ba701877170c6135157beac5f7:ceKCoX1UAx6X/lCfFIhlnxbkdIIj9F77/chdIdukUH8fjpm9AtMjpWsQhT/wYqkC6gWUXG7chHcZsBNJqzYFaw==:1000:9Vd6R+yqPc+VZeY+kYpacy8JmXB52SE51H5hKOyKqshiGcHDsfhT0fSTGT4wDeW8FbL9ITeEK/w5D7hx1qobvt9NT7axiXWfKbug3Rho/bYBkNA7BlZyUYvBhY0o4DJtyWuEtBttVlY7+vvq17jwtHiWNHa+Pq7S2QQioqwy1Kc='),
            ('_px','ceKCoX1UAx6X/lCfFIhlnxbkdIIj9F77/chdIdukUH8fjpm9AtMjpWsQhT/wYqkC6gWUXG7chHcZsBNJqzYFaw==:1000:Dm+RgJSa7opeQx8ZcullSF/FhxU0DI6IGfChg0CQgHvS7/Vm5KJLc0t8Pqxz+WhrV8y5OMivSDVcGuNPcm7TJq65czgu4jj4MI8TmAIo6aarMtyLGazl31LiSuZpGcPOdB0TB0YgwI9mEdlvRgy0ravyNEPit61reyX+hdk+MvNnRY8NuraYHVFXQx98fUVnBbdokPyt1nlm98N+tm+nJ/v5trRcVFE+3lmivFVN1eLK2+gLGTMHjLCH0107D2WXTwY4CIrm//HDvnUv4NpTpA=='),
            ('_uetsid','6a383c9ba03fa131bef77c40f5a02491'),
            ('_uetvid','e9cea5b5bf28069ae40b4b40ca14cce1'),
            ('_cs_cvars','%7B%221%22%3A%5B%22Page%20Name%22%2C%22Auth%20page%22%5D%2C%222%22%3A%5B%22Experience%22%2C%22desktop%22%5D%2C%223%22%3A%5B%22Page%20Type%22%2C%22core%22%5D%2C%224%22%3A%5B%22Auth%20Status%22%2C%22Logged%20Out%22%5D%7D'),
            ('_cs_id', 'aba001e3-c8c6-a69a-e0a6-58bb37d08ccd.1599551932.1.1599552100.1599551932.1.1633715932282.Lax.0'),
            ('_cs_s', '3.1'),
            ('__CT_Data', 'gpv=39&ckp=tld&dm=chegg.com&apv_79_www33=39&cpv_79_www33=39'),
            ('s_pers','%20buFirstVisit%3Dcs%252Ccore%7C1757318332201%3B%20gpv_v6%3Dchegg%257Cweb%257Ccore%257Cauth%2520page%7C1599615555108%3B'),
            ('s_sess','%20buVisited%3Dcs%252Ccore%3B%20s_cc%3Dtrue%3B%20s_ptc%3D0.12%255E%255E0.00%255E%255E0.00%255E%255E0.00%255E%255E0.14%255E%255E0.00%255E%255E1.47%255E%255E0.05%255E%255E1.80%3B%20cheggCTALink%3Dfalse%3B%20SDID%3D3C8B03241E596B2C-40ED395AB7815CA5%3B%20s_sq%3Dcheggincglobal%253D%252526c.%252526a.%252526activitymap.%252526page%25253Dchegg%2525257Cweb%2525257Ccore%2525257Cauth%25252520page%252526link%25253DSign%25252520in%252526region%25253DBODY%252526pageIDType%25253D1%252526.activitymap%252526.a%252526.c%252526pid%25253Dchegg%2525257Cweb%2525257Ccore%2525257Cauth%25252520page%252526pidt%25253D1%252526oid%25253DSign%25252520in%252526oidt%25253D3%252526ot%25253DSUBMIT%3B')
            ],
            'no-outline': None
            }


    # pdfkit.from_url('https://www.chegg.com/homework-help/survey-of-accounting-8th-edition-chapter-a-problem-1e-solution-9781337517386', 'out.pdf', configuration=config,options=options)

    return 
    








