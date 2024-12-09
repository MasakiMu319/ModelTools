#!.venv/bin/python

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import polars as pl
import orjson as json
import numpy as np
import seaborn as sns


plt.rcParams["font.sans-serif"] = ["Songti SC"]  # 用黑体
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题


def interactive_embedding_viz(embeddings, labels, texts):
    tsne = TSNE(n_components=2, perplexity=40, n_iter=300, random_state=42)
    tsne_results = tsne.fit_transform(embeddings)

    fig, ax = plt.subplots(figsize=(16, 10))
    scatter = ax.scatter(
        tsne_results[:, 0],
        tsne_results[:, 1],
        c=[hash(str(label)) for label in labels],
        cmap="tab20",
        alpha=0.6,
    )

    # 创建annotation对象用于显示文本
    annot = ax.annotate(
        "",
        xy=(0, 0),
        xytext=(10, 10),
        textcoords="offset points",
        bbox=dict(boxstyle="round,pad=0.5", fc="yellow", alpha=0.5),
        arrowprops=dict(arrowstyle="->"),
    )

    annot.set_visible(False)

    def hover(event):
        if event.inaxes == ax:
            cont, ind = scatter.contains(event)
            if cont:
                idx = ind["ind"][0]
                annot.xy = (tsne_results[idx, 0], tsne_results[idx, 1])
                annot.set_text(f"文本: {texts[idx]}\n标签: {labels[idx]}")
                annot.set_visible(True)
            else:
                annot.set_visible(False)
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)
    plt.show()


def plot_embeddings_scatter(embeddings, labels):
    # t-SNE降维
    tsne = TSNE(n_components=2, perplexity=40, n_iter=300, random_state=42)
    tsne_results = tsne.fit_transform(embeddings)
    # 创建图形
    plt.figure(figsize=(16, 10))

    # 获取唯一标签并创建颜色映射
    unique_labels = list(set(labels))
    colors = sns.color_palette("husl", len(unique_labels))
    color_map = dict(zip(unique_labels, colors))

    # 绘制散点图
    for label in unique_labels:
        mask = [l == label for l in labels]
        plt.scatter(
            tsne_results[mask, 0],
            tsne_results[mask, 1],
            c=[color_map[label]],
            label=label,
            alpha=0.6,
        )

    # 添加图例
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()


df = pl.read_csv("output-embed.csv")
embeddings = np.array([json.loads(embedding) for embedding in df["embedding"]])
intents = df["intent"].to_list()
labels = []
labels_map = {"2": "育儿", "9": "新闻资讯", "11": "天气情况", "14": "闹钟"}
for label in intents:
    labels.append(labels_map[str(label)])
print(embeddings.shape)
interactive_embedding_viz(embeddings, labels, df["text"].to_list())
# plot_embeddings_scatter(embeddings, labels)
