// assets/marker.js
import React from 'react';
import { Marker as RLMarker, Popup as RLPopup } from 'react-leaflet'
import L from 'leaflet'

export function Marker(params) {
    // console.log(`Marker Parameter: ${JSON.stringify(params)}`)
    const myIcon = L.icon({
        iconUrl: params.data.icon,
        shadowUrl: '/marker-shadow.png',
    });
    let link
    if (params.data.link) {
        link = <p><a target="_blank" href={params.data.link}>link</a></p>
    }
    let zone
    zone = <p class={params.data.zone}><span class="zone">{params.data.zone} zone</span></p>

    let description
    if (params.data.description) {
        description = <p class="description">{params.data.description}</p>
    }
    let opening_hours
    if (params.data.opening_hours) {
        opening_hours = <p class="opening-hours"><strong>Öffnungszeiten</strong>: {params.data.opening_hours}</p>
    }
    let accessibility
    if (params.data.accessibility) {
        accessibility = <p class="accessibility"><strong>Accessibility:</strong> {params.data.accessibility}</p>
    }
    let risk
    if (params.data.risk) {
        risk = <p class="risk"><strong>Risiken:</strong> {params.data.accessibility}</p>
}

  return (
      <RLMarker {...{...params, data:undefined}} icon={myIcon}>
        <RLPopup>
            <div class="youth-map-popup">
                <h1>{params.data.name}</h1>
                {zone}
                {description}
                {opening_hours}
                {accessibility}
                {risk}
                {link}
            </div>
        </RLPopup>
      </RLMarker>
  )
}
