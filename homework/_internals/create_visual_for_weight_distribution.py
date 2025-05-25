from homework._internals.create_docs_folder import create_docs_folder


import matplotlib.pyplot as plt


def create_visual_for_weight_distribution(df):
    df = df.copy()
    plt.figure()
    df.Weight_in_gms.plot.hist(
        title="Shipped Weight Distribution",
        color = "tab:orange",
        edgecolor="white"
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    create_docs_folder()
    plt.savefig("docs/weight_distribution.png")