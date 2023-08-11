#Instructions setting up Battery testing software

# Capacity tests Steps 1-11 are 1st time set up

1. Download Capacity Test.vi from GitHub repository
2. Set up NI MAX / create task from CDaq module named BatteryTemp with two thermocouple temperatures for
   channel 0 and channel 1, and name them BatteryTemp and ChamberTemp. Make sure that sampling type
   is continuous sampling
4. Right-click on Internet icon and open Network and Internet settings
5. In Ethernet tab, click Change Adapter Options
6. Right-click ethernet and open properties
7. click on Internet Protocal Version 4 and open properties
8. Under use following IP Address, enter value between 192.168.0.201 and 192.168.0.254 to connect to NHR module
   If connecting multiple computers to the network, use different IP addresses
9. Open Command Prompt and ping the NHR tester using IP address 192.168.0.93 or 95 etc.
10. Back in NI MAX, Add network device VISA TCP/IP Resource
11. Auto-detect select IP Address of Battery Test
12. Use flashdrive from NHR folder to download Labview drivers onto computer

# Running the Capacity tests
12. Open Capacity Test.vi
13. Once opened in Labview, under VISA resource name select IP address of NHR module
14. Under DAQ task, select BatteryTemp
15. set Current Set Point to C value you want to test
16. set discharge Voltage set point to 2.75 V for 18650 cells
17. In Write to Measurement File, under filename, select the path you want to save the test data to
18. Under output safety, set min/max voltage and current based on the cell and the test you are running
