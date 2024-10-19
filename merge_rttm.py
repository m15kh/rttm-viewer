def merge_rttm_files(file1, file2, output_file="merge_3_intact_oct3_01.rttm"):
    with open(output_file, 'w') as output:
        # Read the first file
        with open(file1, 'r') as f1:
            content1 = f1.readlines()
            output.writelines(content1)
        
        # Read the second file
        with open(file2, 'r') as f2:
            content2 = f2.readlines()
            output.writelines(content2)

    print(f"Files {file1} and {file2} have been merged into {output_file}")

# Example usage
label  = '/home/rteam2/m15kh/rttm-viewer/naser_result_intact_oct3_01_duration(2).rttm'
predict = '/home/rteam2/m15kh/rttm-viewer/merge_intact_oct3_01.rttm'
merge_rttm_files(label , predict)
