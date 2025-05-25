from homework._internals.create_docs_folder import create_docs_folder


import matplotlib.pyplot as plt


def create_visual_for_mode_of_shipment(df):
    df = df.copy()
    plt.figure()
    counts = df.Mode_of_Shipment.value_counts()
    counts.plot.pie(
        title = "Mode of shipment",
        wedgeprops = dict(width= 0.35),
        ylabel = "",
        colors=["tab:blue","tab:orange","tab:green"]
    )
    create_docs_folder()
    plt.savefig("docs/mode_of_shipment.png")