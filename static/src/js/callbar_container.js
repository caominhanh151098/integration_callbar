/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useBus } from '@web/core/utils/hooks';
import { cookie } from "@web/core/browser/cookie";

export class CallbarContainer extends Component {
  static template = "callbar_antbuddy.CallbarContainer";
  setup() {
    window.addEventListener('message', (event) => {
      var data = event.data;
      if (data.from == 'Callbar' && data.type == 'channel_create')
          this.env.bus.trigger("toggle_state", false);
    })
    
    // this.token = cookie.get('token');
    this.src = `https://antbuddy.com/softphone/`;
    this.close = useState({ value:true });


    useBus(this.env.bus, "toggle_state", (event) => {
      this.close.value = event.detail;
    });
  }

  toggleCallbar() {
    this.close.value = !this.close.value;
    this.env.bus.trigger("toggle_state", this.close.value);
  };
}

registry.category("main_components").add("CallbarContainer", {
  Component: CallbarContainer,
});

class SystrayIcon extends Component {
  static template = "systray_icon";
  setup() {
    this.close = useState({ value: true });

    useBus(this.env.bus, "toggle_state", (event) => {
      this.close.value = event.detail;
    });
  }

  toggleCallbar() {
    this.close.value = !this.close.value;
    this.env.bus.trigger("toggle_state", this.close.value);
  };
}

export const systrayItem = {
   Component: SystrayIcon,
};

registry.category("systray").add("SystrayIcon", systrayItem, { sequence: 10 });