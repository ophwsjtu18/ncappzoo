entity_id = data.get('light.hue_color_lamp_1')
rgb_color = data.get('rgb_color', [255, 255, 255])
if entity_id is not None:
    service_data = {'light.hue_color_lamp_1': entity_id, 'rgb_color': rgb_color, 'brightness': 255 }
    hass.services.call('light', 'turn_on', service_data, False)
