import os
from src import config_read, report_config_read
from src.make_report import make_result_for_report
from src.make_report.result_for_report import ResultForReport
from src.make_report import make_graph
from src import graph_writer


def write_row_data(result: ResultForReport):
    output_dir = os.path.join(os.path.abspath("output"), "report", "row")
    os.makedirs(output_dir, exist_ok=True)
    result.result_ideal.to_csv(
        os.path.join(output_dir, "ideal.json"),
    )
    result.result_nominal.to_csv(
        os.path.join(output_dir, "nominal.json"),
    )
    for result_by_wind in result.result_by_wind_speed:
        for result_by_direction in result_by_wind.result:
            result_by_direction.result.to_csv(
                os.path.join(
                    output_dir,
                    f"wind_speed_{result_by_wind.wind_speed}_wind_direction_{result_by_direction.wind_direction}.json",
                )
            )


def run():
    config = config_read.read(os.path.abspath("config"))
    report_config = report_config_read.read(os.path.abspath("config"))
    result = make_result_for_report.make_result_for_report(config, report_config)
    write_row_data(result)

    graphs = make_graph.make_graph(result)
    path_graph = os.path.join(
        os.path.abspath("output"),
        "report",
        "graph",
    )
    os.makedirs(path_graph, exist_ok=True)
    graph_writer.write(
        path=path_graph,
        graphs=graphs,
    )


if __name__ == "__main__":
    run()
