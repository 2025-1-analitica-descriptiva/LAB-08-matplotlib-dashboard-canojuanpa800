from homework._internals.create_docs_folder import create_docs_folder


import matplotlib.pyplot as plt


def create_visual_for_shipping_per_warehouse(df):
    df = df.copy()
    plt.figure()
    counts = df.Warehouse_block.value_counts()
    counts.plot.bar(
        title = "Shipping per Warehouse",
        xlabel = "Warehouse block",
        ylabel = "Record Count",
        color = "tab:blue",
        fontsize = 8
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    create_docs_folder()
    plt.savefig("docs/shipping_per_warehouse.png")