"""
Alan Naoto Tabata
Created: 18/03/2019
Updated: 19/06/2019
"""

import matplotlib.pyplot as plt


class GraphAnalysis:
    def __init__(self, input_files):
        name_id = 2
        year_id = 0
        cites_id = 1
        ignore_first_two_lines = 2
        row_with_labels = 1
        for txt_file in input_files:
            with open(txt_file, 'r') as file:
                lines = file.read().splitlines()
                data = [lines[row_with_labels].split(', ')]
                data = data + [[x.split(', ')[name_id], int(x.split(', ')[year_id]), int(x.split(', ')[cites_id])] for x in lines[ignore_first_two_lines:]]
                if "object_detect_reduced" in txt_file:                    
                    self.boundingbox_content = data
                elif "semantic" in txt_file:
                    self.semantic_content = data
                elif "instance" in txt_file:
                    self.instance_content = data
                elif "real" in txt_file:
                    self.dataset_real_world = data
                elif "depth_estimation_reduced" in txt_file:
                	self.depth_estimation = data
                else:
                    raise Exception('Are you sure the txt files have the correct name? Check their syntax on the main repository')


    def create_charts(self, cites_upper_threshold):
        most_cited_boundingbox = self._create_chart_template(self.boundingbox_content, cites_upper_threshold, 'BoundingBox')
        most_cited_semantic = self._create_chart_template(self.semantic_content, cites_upper_threshold, 'Semantic')
        most_cited_instance = self._create_chart_template(self.instance_content, cites_upper_threshold, 'Instance')
        most_cited_dataset_real_world = self._create_chart_template(self.dataset_real_world, cites_upper_threshold, 'Datasets_real')
        most_cited_depth_estimation = self._create_chart_template(self.depth_estimation, cites_upper_threshold, 'Depth_estimation')
        print('Most cited bounding box algorithms:', most_cited_boundingbox)
        print('Most cited semantic algorithms:', most_cited_semantic)
        print('Most cited instance algorithms:', most_cited_instance)
        print('Most cited depth estimation:', most_cited_depth_estimation)
        print('Most cited datasets real world:', most_cited_dataset_real_world)        


    def _create_chart_template(self, content_list, cites_upper_threshold, figure_name):
        # Order list by quantity of citations
        ordered_list = sorted(content_list[1:], key=lambda x: x[2])  # content_list[1:] so that I don't get the label

        # Check at which index should the bars start being red
        quantity_of_algorithms = len(ordered_list)
        lower_percentile_index = int(quantity_of_algorithms*(1-cites_upper_threshold))        
        most_cited_algorithms = []
        # Begin construction of image
        fig, ax = plt.subplots()
        for index, x in enumerate(ordered_list):
            algorithm = x[0]
            citations = x[2]            
            if index < lower_percentile_index:
                gray = ax.barh(y=algorithm, width=citations, color='0.75')                
            elif index == lower_percentile_index:                
                last_gray_bar_cites = citations                
                gray = ax.barh(y=algorithm, width=citations, color='0.75')
            elif index > lower_percentile_index:
                red = ax.barh(y=algorithm, width=citations, color='r')
                most_cited_algorithms.append([algorithm, x[1], citations])

        # Puts x ticks only for red bars
        red_bar_x_ticks = [x[0] if counter > lower_percentile_index else " " for counter, x in enumerate(ordered_list)]
        plt.yticks(red_bar_x_ticks)
        ax.tick_params(axis='y', labelsize=8)
        # Hides y labels
        # ax.get_yaxis().set_ticks([])

        # Gets rid of the border around the chart
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Puts labeling on the image
        plt.xlabel('Cites')
        plt.ylabel('Papers', rotation=0)
        ax.xaxis.set_label_coords(1.05, 0.02)
        ax.yaxis.set_label_coords(-0.05, 1.0)

        # plt.title(content_list[0][2])
        plt.title('Top 10% cited papers', color='red')
        plt.legend((red, gray),
                   ('≥{} cites'.format(most_cited_algorithms[0][2]), '≤{} cites'.format(last_gray_bar_cites)),
                   loc=4)

        # Leaves a little more space to the left so that the label name can appear entirely
        plt.gcf().subplots_adjust(left=0.17)

        plt.savefig(figure_name)
        plt.close()
        return most_cited_algorithms


if __name__ == "__main__":
    # User input
    # Files with articles with citations
    input_files = ['articles_object_detect_reduced.txt', 'articles_semantic_segmentation.txt', 'articles_instance_segmentation.txt'
    , 'articles_datasets_real_world.txt', 'articles_depth_estimation_reduced.txt']
    cites_upper_threshold = 0.10  # In percentage, from 0.00 to 1.00, the top x% most cited articles

    # Begin processing of data and image plotting
    GraphGenerator = GraphAnalysis(input_files)
    GraphGenerator.create_charts(cites_upper_threshold)

