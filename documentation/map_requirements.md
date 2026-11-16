
# GeoPulse – Map Requirements

## Objective
Visualize retail store locations, GPS movement and customer footfall using Kepler.gl.

## Required Map Layers

1. Store Locations
2. 500-metre Catchment Areas
3. GPS Footfall Points
4. Traffic Heatmap
5. Commercial Zoning Areas

## Store Location Fields

| Field | Data Type | Description |
|---|---|---|
| Store_ID | STRING | Unique store identifier |
| Store_Name | STRING | Store name |
| Latitude | FLOAT | Store latitude |
| Longitude | FLOAT | Store longitude |
| Store_Type | STRING | Existing or proposed |
| Zoning_Type | STRING | Commercial zone |
| Catchment_Radius | INTEGER | Radius in metres |

## Visualization Requirements

- Display stores using map markers.
- Show catchment areas.
- Visualize GPS footfall.
- Compare morning and evening traffic.
- Support Kepler.gl integration.

## Data Validation

- Check latitude and longitude.
- Verify unique Store_ID.
- Identify missing coordinates.
- Verify zoning information.

## Future Enhancements

- H3 hexagon layer.
- 24-hour time slider.
- React map integration.
