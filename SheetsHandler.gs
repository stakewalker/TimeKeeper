// This function is triggered when the Google Apps Script receives a HTTP GET request

function doGet(e) {
  // Extract the 'action' parameter from the request
  var action = e.parameter.action;

  // Open the Google Spreadsheet by its unique ID and get the active sheet
  var sheet = SpreadsheetApp.openById("YOUR_SHEET_ID").getActiveSheet();

  // Create an empty object to store the result
  var result = {};

  // Check the action requested by the client
  if (action == "read") {
    // If the action is 'read', retrieve all data from the sheet
    result.data = sheet.getDataRange().getValues();
  } else if (action == "write") {
    // If the action is 'write', parse the JSON data received from the client
    var data = JSON.parse(e.parameter.data);
    // Find the next available row in the sheet
    var row = sheet.getLastRow() + 1;
    // Write the data to the next available row in the first column
    sheet.getRange(row, 1, 1, data.length).setValues([data]);
    // Set a success flag in the result object
    result.success = true;
  }

  // Convert the result object to a JSON string and set the MIME type to JSON
  return ContentService.createTextOutput(JSON.stringify(result)).setMimeType(ContentService.MimeType.JSON);
}
