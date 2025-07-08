/** @odoo-module **/
import { PhoneField } from "@web/views/fields/phone/phone_field";
import { patch } from "@web/core/utils/patch";

patch(PhoneField.prototype, {
    /**
     * Called when the phone number is clicked.
     *
     * @private
     * @param {MouseEvent} ev
     */
    onClickCall(ev) {
        if (this.props.record._textValues.phone && ev.currentTarget.classList.contains('o_phone_form_link')) {
            const phone = this.props.record._textValues[this.props.name];
            
            setTimeout(() => {
              var callbar = document.getElementById("iframe-dialer").contentWindow;
              callbar.postMessage({
                  type: "call",
                  number: phone
              }, "https://antbuddy.com/softphone/");
              this.env.bus.trigger("toggle_state", false);
            }, 1000);
        }
    },
});
