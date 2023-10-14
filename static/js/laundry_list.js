$(document).ready(function () {
    $("#paid").change(function () {
        if (this.checked) {
            $("#additionalInputs").show();
        } else {
            $("#additionalInputs").hide();
        }
    });

    // Bind the change event to the dropdown
    $("#laundry_category").on("change", updateTable);

    function updateTable() {
        var category = $("#laundry_category").val();
        var weight = parseFloat($("#weight").val()); // Get the entered weight

        // Make an AJAX request to update the table
        $.ajax({
            url: "/get_laundry_data",
            method: "GET",
            data: { laundry_category: category },
            dataType: "json",
            success: function (data) {
                console.log("Received data:", data); // Debug: Log received data

                var tableBody = $("#laundry_table tbody");

                // Clear existing table body content before adding new rows
                tableBody.empty();

                // Initialize the total amount
                var totalAmount = 0;

                // Populate the table with the received data
                for (var i = 0; i < data.length; i++) {
                    var row = $("<tr>");
                    $("<td>").text(data[i].name).appendTo(row);
                    $("<td>").text(data[i].price).appendTo(row);
                    $("<td>").text(weight).appendTo(row); // Display the entered weight
                    var amount = data[i].price * weight;
                    $("<td>").text(amount.toFixed(2)).appendTo(row); // Calculate and display the amount
                    row.appendTo(tableBody);

                    // Add the amount to the total amount
                    totalAmount += amount;
                }

                // Set the total amount in the hidden input field
                $("#amount").val(totalAmount.toFixed(2));
            },
            error: function (error) {
                console.log("Error fetching data: " + error);
            }
        });
    }

    // Bind the input event to the weight input field
    $("#weight").on("input", updateTable);

    $("#amount_from_cus").on("input", function () {
        var enteredAmount = parseFloat($("#amount_from_cus").val());
        var totalAmount = parseFloat($("#amount").val());

        if (!isNaN(enteredAmount) && enteredAmount >= 0) {
            // Calculate the change
            var change = enteredAmount - totalAmount;

            // Update the "change" input field with the calculated change value
            $("#change").val(change.toFixed(2));
        }
    });

});


