from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import re


def create_question() -> pd.DataFrame:
    return pd.DataFrame({
        'DÍVIDA LÍQUIDA - LUCRO LÍQUIDO': [],
        'DIVIDENDOS': [],	
        'Crescimento de receitas lucro >5% ultimos 5 anos': [],
        'P/VP abaixo de 5': [],
        'Líquida/EBITDA é menor que 2': [],
        '+30 anos de mercado? (Fundação)': [],
        'P/L < 30': [],
        'livre de controle ESTATAL ou concentração em cliente único?': [],
        'LUCRO OPERACIONAL>0': [],
        'pesquisa e inovação?': [],
        'Tem uma boa gestão?': [],
        'É líder nacional ou mundial': [],
        'BLUE CHIP?': [],
        'PERENIDADE O setor em que atua +100 anos?': [],     
        
    })

def create_data_frame() -> pd.DataFrame:
    return pd.DataFrame({
        'Empresa': [],
        'Cotação': [],
        'Divida Liquida': [],
        'Custos': [],
        'Lucro Liquido': [],
        'Lucro Bruto': [],
        'Margem Bruta': [],
        'Margem Liquida': [],
        'Divida Bruta': [],
        'Divida Liquida': [],
        'Roic': [],
        'ROE': [],
        'Receita Liquida': [],
        'EBITA': [],
        'EBIT': [],
        'Impostos': [],
        'Margem EBITA': [],
        'Dy': [],
        'P/VP': [],
        'P/L': [],

    })


def extract_string_from_xpath(xpath: str, browser: webdriver.Chrome) -> str:
    return browser.find_element("xpath", xpath).text

def extract_numeric_from_xpath(xpath: str, browser: webdriver.Chrome) -> str:
    value = browser.find_element("xpath", xpath) \
        .text.replace(',', '.')

    scale = None
    if 'Bilhões' in value:
        scale = 1000000000

    elif 'Milhões' in value:
        scale = 1000000

    elif 'Mil' in value:
        scale = 1000

    if '%' in value:
        percentage_text = value.rstrip('%')  # Remove the percentage sign from the end
        return float(percentage_text)
    if '-' == value:
        return float(0)

    if scale:
        return float(re.sub("[^\\d.-]", "", value)) * scale

    return float(re.sub("[^\\d.-]", "", value))


def main():
    # Create a BardAPI client
    

# Print the generated text
    data = create_data_frame()
    question = create_question()
    

    #valor = input('Digite qual empresa deseja pesquisar')
    empresa = input('Digite o codigo da empresa: ')
    

    # Abre o navegador Chrome
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 10)
    # Navega até o site da Amazon
    browser.get("https://investidor10.com.br")

    # Aguarde um tempo para a página carregar completamente

    # time.sleep(3)  # Espere 2 segundos (pode ajustar conforme necessário)

    search_bar = browser.find_element("xpath", "/html/body/div[3]/div/div/section[1]/div/div/div[1]/div/form/div/span/input[2]")
    wait.until(EC.visibility_of(search_bar))
    search_bar.send_keys(empresa)
    search_bar.submit()

      # Espere 5 segundos (pode ajustar conforme necessário)

    first_result = browser.find_element('xpath', '//*[@id="results"]/div/div[2]/div[1]/div/div/a/div/div[1]/img')
    wait.until(EC.visibility_of(first_result))
    first_result.click()

    time.sleep(5)

    #Nome da Empresa
    xpath_company_name = '//*[@id="header_action"]/div[1]/div[2]/h2'
    company_name = extract_string_from_xpath(xpath_company_name, browser)
    
    #Cotação
    xpathprice = '//*[@id="cards-ticker"]/div[1]/div[2]/div/span'
    price = extract_numeric_from_xpath(xpathprice, browser)
    
    #Receita Liquida
    xpath_receita_liquida = '//*[@id="table-balance-results"]/tbody/tr[2]/td[2]/div[1]'
    receita_liquida = extract_numeric_from_xpath(xpath_receita_liquida, browser)

    #EBITA
    xpath_ebita = '//*[@id="table-balance-results"]/tbody/tr[7]/td[2]/div[1]'
    ebita = extract_numeric_from_xpath(xpath_ebita, browser)

    #EBIT
    xpath_ebit = '//*[@id="table-balance-results"]/tbody/tr[6]/td[2]/div[1]'
    ebit = extract_numeric_from_xpath(xpath_ebit, browser)

    #imposto
    xpath_tax = '//*[@id="table-balance-results"]/tbody/tr[8]/td[2]/div[1]'
    tax = extract_numeric_from_xpath(xpath_tax, browser)

    #divida bruta
    xpath_gross_debt = '//*[@id="table-balance-results"]/tbody/tr[9]/td[2]/div[1]'
    gross_debt = extract_numeric_from_xpath(xpath_gross_debt, browser)

    #Divida Liquida
    xpath_divida_liquida = '//*[@id="table-balance-results"]/tbody/tr[10]/td[2]/div[1]'
    divida_liquida = extract_numeric_from_xpath(xpath_divida_liquida, browser)
    
    #Lucro liquido
    xpath_net_revenue = '//*[@id="table-balance-results"]/tbody/tr[5]/td[2]/div[1]'
    net_revenue = extract_numeric_from_xpath(xpath_net_revenue, browser)

    #Lucro Bruto
    xpath_gross_profit = '//*[@id="table-balance-results"]/tbody/tr[4]/td[2]/div[1]'
    gross_profit = extract_numeric_from_xpath(xpath_gross_profit, browser)

    #Custo
    xpath_cost = '//*[@id="table-balance-results"]/tbody/tr[3]/td[2]/div[1]'
    cost = extract_numeric_from_xpath(xpath_cost, browser)

    #margem bruta
    xpath_gross_margin = '//*[@id="table-balance-results"]/tbody/tr[11]/td[2]'
    gross_margin = extract_numeric_from_xpath(xpath_gross_margin, browser)

    #margem ebita
    xpath_ebit_margin = '//*//*[@id="table-balance-results"]/tbody/tr[12]/td[2]'
    ebit_margin = extract_numeric_from_xpath(xpath_ebit_margin, browser)

    #margem liquida
    xpath_net_margin = '//*[@id="table-balance-results"]/tbody/tr[13]/td[2]'
    net_margin = extract_numeric_from_xpath(xpath_net_margin, browser)
    
    #ROE
    xpath_roe = '//*[@id="table-balance-results"]/tbody/tr[14]/td[2]'
    roe = extract_numeric_from_xpath(xpath_roe, browser)

    #roic
    xpath_roic = '//*[@id="table-balance-results"]/tbody/tr[15]/td[2]'
    roic = extract_numeric_from_xpath(xpath_roic, browser)

    xpath_dy = '//*[@id="cards-ticker"]/div[5]/div[2]/span'
    dy= extract_numeric_from_xpath(xpath_dy, browser)

    xpath_pvp = '//*[@id="cards-ticker"]/div[4]/div[2]/span'
    pvp = extract_numeric_from_xpath(xpath_pvp, browser)

    xpath_growth5y = '//*[@id="checklist"]/div/div[1]/div[7]/label/span'
    growth5y = extract_numeric_from_xpath(xpath_growth5y, browser)

    xpath_pl= '//*[@id="cards-ticker"]/div[3]/div[2]/span'
    pl = extract_numeric_from_xpath(xpath_pl, browser)

    data.loc[len(data)] = {\

                           'Empresa': company_name, 'Cotação': price,  \
                           'Divida Liquida': divida_liquida, 'Custos': cost, \
                           'Lucro Bruto': gross_profit, 'Margem Bruta': gross_margin, \
                           'Margem Ebita': ebit_margin, 'Margem Liquida': net_margin, \
                           'Divida Bruta': gross_debt,  'ROE': roe, 'Receita Liquida': receita_liquida, \
                           'EBITA': ebita, 'EBIT': ebit, 'Impostos': tax, \
                           'Margem EBITA': ebit_margin, 'Lucro Liquido': net_revenue, 'Roic': roic, 'Dy': dy,                  
                           'P/VP': pvp, 'P/L': pl                   
 }
    


    question.loc[len(question)] = {\
        'DÍVIDA LÍQUIDA - LUCRO LÍQUIDO': str(1) if float(net_revenue) - float(divida_liquida) > 0 else str(0),
        'DIVIDENDOS': str(1) if float(dy) > 0 else str(0),
        #'Crescimento de receitas lucro >5% ultimos 5 anos': str(1) if growth5y else str(0) 
        'P/VP abaixo de 5': str(1) if float(pvp) < 5 else str(0),
        'Líquida/EBITDA é menor que 2': str(1) if (float(divida_liquida) / float(ebita)) < 2 else str(0),
        'P/L < 30': str(1) if float(pl) < 30 else str(0),
}

    print(data)
    print(question)

    data.to_csv('dados.csv', sep=';', encoding='utf-8', index=False)
    question.to_csv('questions.csv', sep=';', encoding='utf-8', index=False)

    loaded_data = pd.read_csv('dados.csv', sep=';', encoding='utf-8')
    loaded_question = pd.read_csv('questions.csv', sep=';', encoding='utf-8')

    print(loaded_data)
    print(loaded_question)

    browser.quit()

if __name__ == "__main__":
    main()

