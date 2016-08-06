source /home/mslade/exp/trunk/env_scripts/exponent.sh

echo "starting rossman . ."
node machineJS.js /home/mslade/third_party/machineJS/node_modules/data-for-tests/rossman/train.csv --predict /home/mslade/third_party/machineJS/node_modules/data-for-tests/rossman/test.csv
echo "rossman completed.  . ."

echo "starting walmart . . ."
node machineJS.js /home/mslade/third_party/machineJS/node_modules/data-for-tests/wmt/train.csv --predict /home/mslade/third_party/machineJS/node_modules/data-for-tests/wmt/test.csv
echo "walmart completed . . ."

echo "starting givecredit . . "
node machineJS.js /home/mslade/third_party/machineJS/node_modules/data-for-tests/giveCredit/train.csv --predict /home/mslade/third_party/machineJS/node_modules/data-for-tests/giveCredit/test.cs
echo "givecredit completed . . ."


