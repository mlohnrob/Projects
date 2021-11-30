package com.mlohnrob;
import totalcross.ui.MainWindow;
import totalcross.ui.Label;
import totalcross.sys.Settings;
import totalcross.sys.Time;

import com.mlohnrob.ui.Clock;

public class SmartMirror extends MainWindow {
    
    public SmartMirror() {
        setUIStyle(Settings.MATERIAL_UI);
    }

    @Override
    public void initUI() {
				// Time time = new Time();
        // Label clock = new Label(time.hour + ":" + time.minute + "\n" + time.day + "/" + time.month + "/" + time.year);
        // add(clock, CENTER, 50);

				// while (true) {
				// 		time.update();
				//		clock.setText(time.hour + ":" + time.minute + "\n" + time.day + "/" + time.month + "/" + time.year);
				// }
				


				Clock clock = new Clock();
				add(clock, CENTER, 50);

    }
}
