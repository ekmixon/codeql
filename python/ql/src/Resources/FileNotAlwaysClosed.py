with open("filename") as f:
    ... # Actions to perform on file
# File only closed if actions are completed successfully

with open("filename") as f:
    ...# Actions to perform on file
# File always closed

f = open("filename")
try:
    ... # Actions to perform on file
finally:
    f.close()
# File always closed
