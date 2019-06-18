"""
Alan Naoto Tabata
Created: 18/03/2019
Updated: 18/03/2019
"""

import matplotlib.pyplot as plt


class GraphAnalysis:
    def __init__(self):
        pass

    def readInputs(self, inputFile):
        with open(inputFile, 'r') as file:
            lines = file.read().splitlines()

        # Creates index breakpoints when collecting each article entry
        semanticIndex = lines.index('## Open source algorithms on semantic segmentation')
        instanceIndex = lines.index("## Open source algorithms on instance segmentation")
        semanticContent = lines[semanticIndex+1:instanceIndex]
        instanceContent = lines[instanceIndex+1:]

        self.semanticContent = [[x.split(', ')[2], int(x.split(', ')[0]), int(x.split(', ')[1])] for x in semanticContent[1:]]
        self.instanceContent = [[x.split(', ')[2], int(x.split(', ')[0]), int(x.split(', ')[1])] for x in instanceContent[1:]]

        self.semanticContent = [semanticContent[0].split(', ')] + self.semanticContent
        self.instanceContent = [instanceContent[0].split(', ')] + self.instanceContent

    def createCharts(self, citesUpperThreshold, showImages):
        mostCitedSemantic = self._createChartTemplate(self.semanticContent, citesUpperThreshold, showImages)
        mostCitedInstance = self._createChartTemplate(self.instanceContent, citesUpperThreshold, showImages)
        print('Most cited semantic algorithms:', mostCitedSemantic)
        print('Most cited instance algorithms:', mostCitedInstance)

    def _createChartTemplate(self, contentList, citesUpperThreshold, showImages):
        # Order list by quantity of citations
        orderedList = sorted(contentList[1:], key=lambda x: x[2])  # contentList[1:] so that I don't get the label

        # Check at which index should the bars start being red
        quantityOfAlgorithms = len(orderedList)
        indexStartTopAlgorithms = quantityOfAlgorithms - int(quantityOfAlgorithms * citesUpperThreshold)
        mostCitedAlgorithms = []

        # Begin construction of image
        fig, ax = plt.subplots()
        for index, x in enumerate(orderedList):
            algorithm = x[0]
            citations = x[2]
            if index >= indexStartTopAlgorithms:
                red = ax.barh(y=algorithm, width=citations, color='r')
                mostCitedAlgorithms.append([algorithm, x[1], citations])
            else:
                gray = ax.barh(y=algorithm, width=citations, color='0.75')

        # Puts x ticks only for red bars
        redBarXTicks = [x[0] if counter >= indexStartTopAlgorithms else " " for counter, x in enumerate(orderedList)]
        plt.yticks(redBarXTicks)

        # Gets rid of the border around the chart
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Puts labeling on the image
        plt.xlabel('Number of citations')
        plt.title(contentList[0][2])
        plt.legend((red, gray),
                   ('>={} cites'.format(mostCitedAlgorithms[0][2]), '<{} cites'.format(mostCitedAlgorithms[0][2])),
                   loc=4)

        # Leaves a little more space to the left so that the label name can appear entirely
        plt.gcf().subplots_adjust(left=0.15)

        plt.savefig(algorithm)
        if showImages:
            plt.show()
        plt.close()
        return mostCitedAlgorithms


if __name__ == "__main__":
    # User input
    inputFile = "articles.txt"  # Path to file with articles with citations
    citesUpperThreshold = 0.10  # In percentage, from 0-1, the top x% most cited articles
    showImages = False # True or False

    # Begin processing of data and image plotting
    GraphGenerator = GraphAnalysis()
    GraphGenerator.readInputs(inputFile)
    GraphGenerator.createCharts(citesUpperThreshold, showImages)


