#!bin/bash

sudo su <<EOF
cd /home/ec2-user/pythoncode/githubdata && echo "success" || echo "failed"

rm -rf coronaboard_kr && echo "success" || echo "failed"

git clone https://github.com/jooeungen/coronaboard_kr.git && echo "success" || echo "failed"

cd /home/ec2-user/pythoncode/ && echo "success" || echo "failed"

python3 imptords.py && echo "success" || echo "failed"
EOF
