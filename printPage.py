from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QMenuBar, QAction, QTextEdit, QFontDialog, QColorDialog, QFileDialog, QWidget, QScrollArea, QVBoxLayout, QFrame
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtCore import QFileInfo, QFile, QTextStream, QRect, Qt


class Window(QMainWindow):
    def __init__(self, form_data):
        super().__init__()

        self.title = "PyQt5 TextEdit"
        self.left = 500
        self.top = 200
        self.width = 500
        self.height = 400
        self.iconName = "home.png"
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        data = form_data
        print(data)

        self.createEditor(data)

        self.CreateMenu()

        self.show()

    def CreateMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        viewMenu = mainMenu.addMenu("View")
        helpMenu = mainMenu.addMenu("Help")
        
        printAction = QAction(QIcon("print.png"), 'Print', self)
        printAction.triggered.connect(self.printDialog)
        printAction.setShortcut("Ctrl+P")
        fileMenu.addAction(printAction)

        printpreviewAction = QAction(QIcon("printpreview.png"), 'Print Preview', self)
        printpreviewAction.triggered.connect(self.printPreviewDialog)
        fileMenu.addAction(printpreviewAction)

        pdfAction = QAction(QIcon("pdf.png"), 'Export PDF', self)
        pdfAction.triggered.connect(self.pdfExport)
        fileMenu.addAction(pdfAction)
        
        exitAction = QAction(QIcon("exit.png"), 'Exit', self)
        exitAction.setShortcut("Ctrl+E")
        exitAction.triggered.connect(self.exitWindow)
        fileMenu.addAction(exitAction)

        copyAction = QAction(QIcon("Copy.png"), 'Copy', self)
        copyAction.setShortcut("Ctrl+C")
        editMenu.addAction(copyAction)

        cutAction = QAction(QIcon("Cut.png"), 'Cut', self)
        cutAction.setShortcut("Ctrl+X")
        editMenu.addAction(cutAction)  

        saveAction = QAction(QIcon("Save.png"), 'Save', self)
        saveAction.setShortcut("Ctrl+S")
        editMenu.addAction(saveAction)  

        pasteAction = QAction(QIcon("Paste.png"), 'Paste', self)
        pasteAction.setShortcut("Ctrl+V")
        editMenu.addAction(pasteAction)  
        
        fontAction = QAction(QIcon("font.png"), 'Font', self)
        fontAction.setShortcut("Ctrl+F")
        fontAction.triggered.connect(self.fontDialog)
        viewMenu.addAction(fontAction)

        colorAction = QAction(QIcon("color.png"), 'Color', self)
        editMenu.addAction(colorAction)  
        colorAction.triggered.connect(self.colorDialog)

        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(copyAction)
        toolbar.addAction(cutAction)
        toolbar.addAction(pasteAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(exitAction)
        toolbar.addAction(fontAction)
        toolbar.addAction(colorAction)
        toolbar.addAction(printAction)
        toolbar.addAction(printpreviewAction)
        toolbar.addAction(pdfAction)

    def exitWindow(self):
        self.close()

    def createEditor(self, data):
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1000, 1500))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setAlignment(Qt.AlignHCenter)
        
        self.textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setFixedSize(1123,1588)
        self.textEdit.setFontFamily("Times New Roman")

        self.textEdit.setAlignment(Qt.AlignHCenter)
        self.textEdit.setFontPointSize(10)
        self.textEdit.setFontWeight(7000)
        self.textEdit.insertPlainText("             CÔNG AN TỈNH ...   CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM")
        self.textEdit.insertPlainText("\nCÔNG AN ...                       Độc lập - Tự do - Hạn phúc     ")
        self.textEdit.append("")


        self.textEdit.setAlignment(Qt.AlignLeft)
        self.textEdit.setFontWeight(700)
        self.textEdit.insertPlainText("\nSố: ... /BB-VPHC")
        self.textEdit.append("")

        self.textEdit.setAlignment(Qt.AlignHCenter)
        self.textEdit.setFontPointSize(11)
        self.textEdit.setFontWeight(7000)
        self.textEdit.insertPlainText("\nBIÊN BẢN VI PHẠM HÀNH CHÍNH")
        self.textEdit.insertPlainText("\nVề lĩnh vực giao thông đường bộ")
        self.textEdit.append("")
        
        self.textEdit.setFontPointSize(10)
        self.textEdit.setAlignment(Qt.AlignLeft)
        self.textEdit.setFontWeight(700)
        self.textEdit.insertPlainText("\nHôm nay, hồi ... giờ ... phút, ngày ... /... /......, tại:........")
        self.textEdit.insertPlainText("\nLý do lập biên bản tại <trụ sở cơ quan của người có thẩm quyền lập biển bản/ địa điểm khác>")
        self.textEdit.insertPlainText("\nCăn cứ: ... ")
        self.textEdit.insertPlainText("\nChúng tôi gồm")
        self.textEdit.insertPlainText("\n1. Người có thẩm quyền lập biên bản:\nHọ và tên: ... Chức năng: ... Cơ quan: Công an thành phố Bắc Ninh.")
        self.textEdit.insertPlainText("\n2. Với người chứng kiến của:\nHọ và tên: ... Nghề nghiệp: ... Địa chỉ: ... \nHọ và tên: ... Chức vụ: ... Cơ quan: ... ")
        self.textEdit.insertPlainText("\n3. Người phiên dịch:\nHọ và tên: ... Nghề nghiệp: ... Địa chỉ: ... ")
        
        self.textEdit.setFontWeight(7000)
        self.textEdit.insertPlainText("\nTiến hành lập biên bản vi phạm hành chính đối với ông(bà)/tổ chức có tên sau đây:")
        self.textEdit.setFontWeight(700)
        self.textEdit.insertPlainText("\n1. Ông(Bà)/Tổ chức(Tên tổ chức, người đại diện theo pháp luật, chức danh): " + data['name'] + "\nGiới tính: " + data['gender'] + " Ngày, tháng, năm, sinh: " + data['birth_year'] + " Quốc tịch: " + data['nationality'] + " Nghề nghiệp/Lĩnh vực hoạt động hoặc Mã số doanh nghiệp: ... Nơi ở hiện tại/Địa chỉ trụ sở: ... Số định danh cá nhân/CMND/CCCD/hộ chiếu/GCN đăng ký đầu tư hoặc GP thành lập số: ... \nNgày: ... / ... / ... .Nơi cấp: ... ")
        self.textEdit.insertPlainText("\n2. Đã có các hành vi vi phạm hành chính: Vào hồi ... giờ ... phút, ngày ... / ... / ... , tại: ... ")
        self.textEdit.insertPlainText("\n3. Quy định tại (Điểm, Khoản, Điều): ... .Nghị định số 100/2019/NĐ-CP ngày 30/12/2019 (sửa đổ, bổ sung tại Nghị điịnh số 123/2021/NĐ-CP ngày 28/12/2021) của Chính phủ quy định xử phạt vi phạm hành chính trong lĩ vực giao thông Đường bộ và Đường sắt.")
        self.textEdit.insertPlainText("\n4. Cá nhân/tổ chức bị thiệt hại (nếu có): ... ")
        self.textEdit.insertPlainText("\n5. Ý kiến trình bày của cá nhân/người đại diện của tổ chức vi phạm: ... ")
        self.textEdit.insertPlainText("\n6. Ý kiến trình bày của đại diện chính quyền, người chứng kiến(nếu có): ... ")
        self.textEdit.insertPlainText("\n7. Ý kiến trình bày của cá nhân/ tổ chức bị thiệt hại (nếu có): ... ")
        self.textEdit.insertPlainText("\n8. Chúng tôi đã yêu cầu cá nhân/tổ chức vi phạm chấm dứt ngay hành vi vi phạm.")
        self.textEdit.insertPlainText("\n9. Các biện pháp ngăn chặn và bảo đảm xử lý vi phạm hành chính được áp dụng gồm: ... ")
        self.textEdit.insertPlainText("\n10. Trong thời gian không quá 02 ngày làm việc trong trường hợp cá nhân/người đại diện của tổ chức vi phạm yêu cầu giải trình trực tiếp, không quá 05 ngày làm việc trong trường hợp cá nhân/người đại diện của tổ chức vi phạm giải trình bằng văn bản kể từ ngày lập biên bản này, Ông(Bà)/Tổ chức: ... là cá nhân vi phạm/người đại diện tổ chức vi phạm có quyền gửi văn bản yêu cầu được giải trình trực tiếp/văn bản giải trình đến: ... để thực hiện quyền giải trình.")
        self.textEdit.insertPlainText("\n11. Yêu cầu Ông(Bà)/Tổ chức: ... có mặt vào hồi: ... giờ ... phút ... ngày ... / ... / ...  tại	TP Bắc Ninh, Bắc Ninh để giải quyết vụ việc.")
        self.textEdit.insertPlainText("\nBiên bản lập xong hồi ... giờ ... phút, ngày ... / ... / ... , gồm 01 tờ, được lập thành 2 bản có nội dung, giá trị như nhau; đã đọc lại cho những người có tên nêu trên cùng nghe, công nhận là đúng và cùng ký tên dưới đây; giao cho ông (bà) ... là cá nhân/người đại diện của tổ chức vi phạm 01 bản hoặc cha, mẹ/người giám hộ của người chưa thành niên vi phạm 01 bản, 01 bản lưu hồ sơ.")
        self.textEdit.insertPlainText("\nLý do ông (bà) ... vi phạm không ký biên bản: ... \nLý do ông (bà) ... không ký xác nhận: ... ")
        self.textEdit.append("")
    
        self.textEdit.setAlignment(Qt.AlignHCenter)
        self.textEdit.setFontPointSize(8)
        self.textEdit.setFontWeight(7000)
        self.textEdit.insertPlainText("\nCÁ NHÂN/NGƯỜI ĐẠI DIỆN     CÁ NHÂN/NGƯỜI ĐẠI DIỆN      NGƯỜI CHỨNG KIẾN/ĐẠI DIỆN    NGƯỜI PHIÊN DỊCH    NGƯỜI LẬP BIÊN BẢN ")

        self.verticalLayout_2.addWidget(self.textEdit)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.setCentralWidget(self.frame)


    def fontDialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.textEdit.setFont(font)
    
    def colorDialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.accepted:
            self.textEdit.print_(printer)

    def printPreviewDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.printPreview)
        previewDialog.exec_()

    def printPreview(self, printer):
        self.textEdit.print_(printer)

    def pdfExport(self):
        fn, _=QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf);;All Files()")

        if fn != '':

            if QFileInfo(fn).suffix() == "":fn += '.pdf'

            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print_(printer)
if __name__ == "__main__":
    import sys   
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
