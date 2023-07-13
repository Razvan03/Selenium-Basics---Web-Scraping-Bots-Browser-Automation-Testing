<%@ Page Language="C#" AutoEventWireup="true" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Simple Form</title>
</head>
<body>
    <form id="form1" runat="server">
        <h2>Message Box</h2>
        <asp:Label ID="Label1" runat="server" Text="Please enter your message:"></asp:Label>
        <asp:TextBox ID="TextBoxMessage" runat="server"></asp:TextBox>
        <button type="button" onclick="return showMessage()">Show Message</button>
        <asp:Label ID="Message" runat="server"></asp:Label>
        
        <h2>Calculation Box</h2>
        <asp:Label ID="Label3" runat="server" Text="Enter A:"></asp:Label>
        <asp:TextBox ID="TextBoxA" runat="server"></asp:TextBox>
        <asp:Label ID="Label4" runat="server" Text="Enter B:"></asp:Label>
        <asp:TextBox ID="TextBoxB" runat="server"></asp:TextBox>
        <button type="button" onclick="return calculateTotal()">Get Total</button>
        <asp:Label ID="Total" runat="server"></asp:Label>
    </form>

    <!-- Custom pop-up message box -->
    <div id="myModal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <p>This is a pop-up message box.</p>
            <button id="popupButton">OK</button>
        </div>
    </div>

    <style>
        /* Style for the modal box */
        .modal {
            display: none;
            position: fixed;
            z-index: 1;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgba(0, 0, 0, 0.4);
        }

        .modal-content {
            background-color: #fefefe;
            margin: 15% auto;
            padding: 20px;
            border: 1px solid #888;
            width: 80%;
        }

        .close {
            color: #aaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
        }

        .close:hover,
        .close:focus {
            color: black;
            text-decoration: none;
            cursor: pointer;
        }
    </style>

    <script>
        // Show the pop-up message box when the page loads for the first time
        window.onload = function () {
            var isFirstLoad = sessionStorage.getItem("isFirstLoad");
            if (!isFirstLoad) {
                var modal = document.getElementById("myModal");
                modal.style.display = "block";
                sessionStorage.setItem("isFirstLoad", "true");
            }
        }

        // Close the pop-up message box when the close button is clicked
        var closeBtn = document.getElementsByClassName("close")[0];
        closeBtn.onclick = function () {
            var modal = document.getElementById("myModal");
            modal.style.display = "none";
        }

        // Button click event in the pop-up message box
        var popupButton = document.getElementById("popupButton");
        popupButton.onclick = function () {
            var modal = document.getElementById("myModal");
            modal.style.display = "none";
        }

        // Function to show the message
        function showMessage() {
            var textBoxMessage = document.getElementById("<%= TextBoxMessage.ClientID %>");
            var message = document.getElementById("<%= Message.ClientID %>");
            message.innerHTML = "Your Message: " + textBoxMessage.value;
            return false; // Prevent form submission
        }

        // Function to calculate the total
        function calculateTotal() {
            var textBoxA = document.getElementById("<%= TextBoxA.ClientID %>");
            var textBoxB = document.getElementById("<%= TextBoxB.ClientID %>");
            var totalLabel = document.getElementById("<%= Total.ClientID %>");
            var a = parseInt(textBoxA.value);
            var b = parseInt(textBoxB.value);
            var total = a + b;
            totalLabel.innerHTML = "Total a + b = " + total;
            return false; // Prevent form submission
        }
    </script>
</body>
</html>