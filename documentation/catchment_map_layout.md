
# GeoPulse – Catchment Area Map Layout

## 1. Objective
Design a map to visualize GPS movements around retail store locations and their catchment areas.

## 2. Required GPS Fields
- DeviceID
- Latitude
- Longitude
- Timestamp

## 3. Required Store Fields
- StoreID
- Store_Name
- Store_Latitude
- Store_Longitude

## 4. Map Layers

### Layer 1: Store Locations
Display retail stores using map markers.

### Layer 2: GPS Movement
Display device GPS points using latitude and longitude.

### Layer 3: Catchment Areas
Display a planned 500-metre radius around each store.

## 5. Map Filters
- Store ID
- Date
- Time

## 6. Expected Output
An interactive Kepler.gl map showing store locations, GPS points and planned catchment areas.

## 7. Pending Activities
- Generate actual 500-metre catchment polygons.
- Perform spatial joins.
- Validate GPS points against store catchment areas.

## 8. Status
Day 6 map layout and required field planning documented.
Actual spatial processing is pending.
