# velodyne_analysis
Analyse Velodyne data from old data sets (rosbag).

The problem for the old data sets is that the message types for the raw data are `VelodyneRawScan` and `velodyneRawPacket`, while in the ros package **velodyne_pointcloud** (for turning velodyne raw data into pointcloud2) the required message types are `VelodyneScan` and `velodynePacket`. These differences will make the conversion fail.

The simple solution using now is to subscribe the original topic `/driving/velodyne/raw_packets` (original data type `VelodyneRawScan`) by the message type `VelodyneScan` and simply replublish it with the same data type. This way, we could then successfully transform velodyne raw data into pointcloud2.

The above mentioned method would be applied with the following command:
```
roslaunch velodynePointcloud boschBagConvert.launch
```

## Full procedure 
First play the rosbag from Bosch
```
rosbag play payh_to_bag_file
```
Then launch the `boschBagConvert.launch`
```
roslaunch velodynePointcloud boschBagConvert.launch
```
The resulting data `/velodyne_points` would be in data type `PointCloud2`
