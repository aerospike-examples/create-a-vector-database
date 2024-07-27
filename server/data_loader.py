import csv

__MORTGAGE = 'Mortgage Product'
__SAVINGS = 'Savings Product'
__CHECKING = 'Checking Product'
__CREDIT_CARD = 'Credit Card Product'
__MUTUAL_FUNDS = 'Mutual Funds'
__LINE_OF_CREDIT = 'Line of Credit'
__WEALTH_MGMT = 'Wealth Management'

def __get_default_products():
    return [
        {
            'type': __MORTGAGE, 
            'name': "Swamp Leasing", 
            'feature': 'Lending for the leasing of swamps. Primarily focused '
                        'around murky swamps for ogres, but other creatures may use this product.'
        },
        {
            'type': __SAVINGS, 
            'name': 'High Flying Saver', 
            'feature': 'This product offers a very high interest rate, 2% higher than the standard rate.'
                        'It may only be used by creatues with the capability to fly, dragons, griffins, fairies, pegasi and so on'
        },
        {
            'type': __SAVINGS,
            'name':'Griffin Savings Account',
            'feature':'Roar into savings with our Griffin-exclusive account. Enjoy high-interest rates that '
                        'soar as high as you do! (Feathers not required for deposits.)'
        },
        {
            'type':__CHECKING,
            'name':'Centaur Checking',
            'feature':'Half-human, half-horse, fully convenient! Manage your finances effortlessly with our mobile '
                        'banking app, designed with extra legroom for centaurs.'
        },
        {
            'type':__SAVINGS,
            'name':'Centaur Savings Account',
            'feature':'A hybrid savings account where customers can earn interest in “horsepower.” The more horsepower you have, the faster your savings grow—perfect for those who like to gallop to the bank.'
        },
        {
            'type': __MORTGAGE,
            'name': 'Mermaid Mortgage',
            'feature':'Make waves in the housing market with our tailored mortgage options for merfolk. Our '
                        'sea-worthy rates will keep you anchored to your dream home.'
        },
        {
            'type': __SAVINGS,
            'name': 'Mermaid Money Maker',
            'feature': 'A shimmering account that allows mermaids to earn a high interest rate in "sea pearls." '
                        'Withdrawals are only permitted during high tide to avoid pesky sea currents.'
        },
        {
            'name' : __CREDIT_CARD,
            'name':'Phoenix Credit Card',
            'feature':'Burn through expenses and rise from the ashes of debt with our Phoenix Credit Card. Earn '
                        'fiery rewards and never fear a late payment again.'
        },
        {
            'type' : __MUTUAL_FUNDS,
            'name':'Minotaur Mutual Funds',
            'feature':"Navigate the labyrinth of investment opportunities with our Minotaur Fund Managers. "
                        "They'll guide you through the bull market like true professionals."
        },
        {
            'type': __SAVINGS,
            'name':'Dragon Treasure Vaults',
            'feature':"Protect your hoard with our state-of-the-art vaults, designed exclusively for dragons. "
                        "Fireproof, theft-proof, and envy-proof—because every dragon deserves peace of mind."
        },
        {
            'type': __MORTGAGE,
            'name':"Dragon's Den Home Loan",
            'feature':"A loan specifically for dragons looking to expand their hoards. The interest rate is based "
                        "on the amount of gold you're hoarding, and if you can breathe fire, you get a special discount!"
        },
        {
            'type': __LINE_OF_CREDIT,
            'name':'Goblin Gold Loans',
            'feature':"Need gold in a pinch? Our Goblin Gold Loans offer quick approvals and competitive rates, "
                        "perfect for when you're short on shiny things."
        },
        {
            'type': __LINE_OF_CREDIT,
            'name':'Witches Brew-ery',
            'feature':'A loan service for witches looking to brew their own potions. Repayment can be done in '
                        'spells, or you can opt for “easy broomstick payments” to fly under the radar!'
        },
        {
            'type': __CREDIT_CARD,
            'name':'Chimera Credit Card',
            'feature':"A credit card that lets you accumulate points for every creature you transform into. Earn "
                        "double points when using it to purchase mythical creature accessories—like a three-headed dog collar!"
        },
        {
            'type': __WEALTH_MGMT,
            'name':'Fairy Financial Planning',
            'feature':"Let our expert fairies sprinkle some magic on your financial future. From "
                        "retirement plans to enchanted savings strategies, they'll make your money grow like pixie dust."
        },
        {
            'type': __WEALTH_MGMT,
            'name':'Werewolf Wealth Management',
            'feature':"Moonlighting as an investor? Our Werewolf Wealth Management team understands "
                        "the wild ups and downs of the market. Trust us to howl at the moon for your financial success."
        },
        {
            'type': __SAVINGS,
            'name': 'Vampire Vault Account',
            'feature': "Keep your assets safe from sunlight and other hazards with our Vampire Vault "
                        "Account. Perfect for nocturnal withdrawals and secure transactions."
        },
        {
            'type': __SAVINGS,
            'name': 'Yeti Snowball Savings',
            'feature': 'A fund dedicated to Yetis who need cash for snowball emergencies. Withdrawals are permitted '
                        'only during snowstorms, with a limit on how many snowballs you can buy!'
        },
        {
            'type': __SAVINGS,
            'name': 'Kraken Seaside Savings',
            'feature': "A long-term investment that's safe as long as you don't disturb the deep sea. Beware of "
                        "unexpected withdrawals when the Kraken gets hungry—investments may take a while to surface!"
        },
        {
            'type': __CHECKING, 
            'name': 'Check this out!', 
            'feature': "Want a super checking account which doesn't compromise on features? Look no further than this. "
                        "Ideal for unicorns, giants and most other mythological folk. Sadly, this product is not available "
                        "to dragons due to the difficulty of making fire-proof checks."
        }
    ]

# Create a data file with the default products
def create_products(file: str):
    products = __get_default_products()
    with open(file, mode='w',newline='') as file:
        fieldnames = ['type', 'name', 'feature']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

def append_product(file: str, product):
    with open(file, mode='a',newline='') as file:
        fieldnames = ['type', 'name', 'feature']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(product)

def read_products(file: str):
    results = []
    with open(file, mode='r',newline='') as file:
        fieldnames = ['type', 'name', 'feature']
        reader = csv.DictReader(file, fieldnames=fieldnames)
        next(reader, None)  # Skip over the header
        for row in reader:
            results.append(row)
    return results

#DATA_FILE = '../data/products.csv'
#create_products(DATA_FILE)
#read_products(DATA_FILE)