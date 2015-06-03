package org.xwalk.embedded.api.sample;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;

public class ContactExtensionActivity extends XWalkActivity {
    private ExtensionContact mExtension;
    private XWalkView mXWalkView;

	@Override
	protected void onXWalkReady() {
		// TODO Auto-generated method stub
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies extension can be supported .\n\n")
        .append("Test  Step:\n\n")
        .append("1. Input one contact name and contact phone number.\n\n")
        .append("2. Click Write Contact button\n\n")
        .append("3. Click Read Contact button\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if the display of Write & Read contact contains 'passed' in green color.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        setContentView(R.layout.xwview_layout);
        mExtension = new ExtensionContact(ContactExtensionActivity.this);
        
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        mXWalkView.load("file:///android_asset/contact.html", null);
	}

}
