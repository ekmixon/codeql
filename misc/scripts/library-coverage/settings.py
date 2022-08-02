import sys

generated_output_rst = "framework-coverage-{language}.rst"
generated_output_csv = "framework-coverage-{language}.csv"

index = 3 if sys.argv[0].endswith("generate-report.py") else 1
data_prefix = f"{sys.argv[index]}/" if len(sys.argv) > index else ""
documentation_folder_no_prefix = "{language}/documentation/library-coverage/"
documentation_folder = data_prefix + documentation_folder_no_prefix

output_rst_file_name = "coverage.rst"
output_csv_file_name = "coverage.csv"
repo_output_rst = documentation_folder + output_rst_file_name
repo_output_csv = documentation_folder + output_csv_file_name

languages = ['java', 'csharp']
