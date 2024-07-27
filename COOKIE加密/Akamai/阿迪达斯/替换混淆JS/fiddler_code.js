
function OnBeforeResponse(oSession: Session) {
    // 拦截特定的 URL
    var targetUrl = "q9gmug/xT8Yfh/cHJe/kvcivy/to/NEYfkrDmaiDrkiYm/NF0eYBMRMgs/Hjdl/JggZdHY";
    var file_path = "D:\\Projects\\JSProjects\\COOKIE加密\\Akamai\\阿迪达斯\\替换混淆JS\\modify_response.txt"
    if (oSession.uriContains(targetUrl) && oSession.HTTPMethodIs("GET")) {
        try {
            var fso = new ActiveXObject("Scripting.FileSystemObject");
            var file = fso.OpenTextFile(file_path, 1); // 替换为实际文件路径
            var modifiedResponse = file.ReadAll();
            file.Close();

            oSession.utilDecodeResponse();
            oSession.utilSetResponseBody(modifiedResponse);
        } catch (e) {
            FiddlerApplication.Log.LogString("Error reading file: " + e.message);
        }
    }
}
