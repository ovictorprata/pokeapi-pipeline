from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

def categorize_base_experience(base_experinece):
    category =  None
    if base_experinece < 50:
        category = 'Fraco'
    elif base_experinece <= 100:
        category = 'Médio'
    else:
        category = 'Forte'
    return category


def get_df_pokemon_by_type(df_pokemons):
    exploded_types = df_pokemons['Tipos'].explode()
    df_type_count = exploded_types.value_counts().reset_index()
    df_type_count.columns = ['Tipos', 'Quantidade']
    return df_type_count
 
def plot_pokemon_type_distribution(df_type_count):
    ax = sns.barplot(x='Tipos', y='Quantidade', data=df_type_count, errwidth=0, color='#009efa')
    for container in ax.containers:
        ax.bar_label(container)
    ax.set_title('Quantidade de pokemons por tipo', fontweight='bold', fontsize=16)
    ax.set_xlabel('Tipo', fontweight='bold') 
    ax.set_ylabel('Quantidade', fontweight='bold')
    plt.show()