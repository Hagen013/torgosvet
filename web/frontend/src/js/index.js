import {MDCRipple, MDCRippleFoundation, util} from '@material/ripple';

const surfaces = document.getElementsByClassName('ripple')

for (let i=0; i < surfaces.length; i++) {
    MDCRipple.attachTo(surfaces[i]);
}