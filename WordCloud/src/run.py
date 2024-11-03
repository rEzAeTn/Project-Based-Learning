import matplotlib.pyplot as plt
from wordcloud import WordCloud


class WordCloudGenerator:
    def __init__(self, file_path):
        # open file and create Data
        with open(file_path) as f:
            self.text = f.read()


    def run(self, output_path, **kwargs):
        # Create Object from WordCloud
        wordcloud = WordCloud(
        **kwargs
        ).generate(self.text)

        # Data Visualization from matplotlib
        plt.imshow(wordcloud)
        plt.axis('off')

        # save output as image
        wordcloud.to_file(output_path)


if __name__ == '__main__':
    wc_gen = WordCloudGenerator('src/data/movies.txt')
    wc_gen.run('OutPut.png')