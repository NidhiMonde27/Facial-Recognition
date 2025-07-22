# from PyQt5.QtGui import QImage, QPixmap
# from PyQt5.uic import loadUi
# from PyQt5.QtCore import pyqtSlot, QTimer, QDate, Qt
# from PyQt5.QtWidgets import QDialog, QMessageBox
# import cv2
# import face_recognition
# import numpy as np
# import datetime
# import os
# import csv
# from PIL import Image as PILImage

# class Ui_OutputDialog(QDialog):
#     def __init__(self):
#         super(Ui_OutputDialog, self).__init__()
#         self.encode_list = None
#         self.class_names = None
#         loadUi("./outputwindow.ui", self)

#         now = QDate.currentDate()
#         current_date = now.toString('ddd dd MMMM yyyy')
#         current_time = datetime.datetime.now().strftime("%I:%M %p")

#         self.Datelabel.setText(current_date)
#         self.Timelabel.setText(current_time)
#         self.image = None

#     @pyqtSlot()
#     def startVideo(self, camera_name):
#         if len(camera_name) == 1:
#             self.capture = cv2.VideoCapture(int(camera_name))
#         else:
#             self.capture = cv2.VideoCapture(camera_name)
#         self.timer = QTimer(self)
#         path = 'ImagesAttendance'
#         if not os.path.exists(path):
#             os.mkdir(path)

#         images = []
#         self.class_names = []
#         self.encode_list = []
#         self.TimeList1 = []
#         self.TimeList2 = []
#         attendance_list = os.listdir(path)

#         # Load and validate images
#         for cl in attendance_list:
#             img_path = os.path.join(path, cl)
#             try:
#                 # First try with PIL for better format handling
#                 pil_img = PILImage.open(img_path).convert('RGB')
#                 img_array = np.array(pil_img)
                
#                 # Convert to BGR for OpenCV compatibility
#                 img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
                
#                 # Then convert back to RGB for face_recognition
#                 rgb_img = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
                
#                 images.append(rgb_img)
#                 self.class_names.append(os.path.splitext(cl)[0])
#             except Exception as e:
#                 print(f"Error loading image {cl}: {str(e)}")
#                 continue

#         # Process encodings
#         for img in images:
#             try:
#                 # Ensure proper image format
#                 if img.dtype != np.uint8:
#                     img = img.astype(np.uint8)
                
#                 # Detect faces and encodings
#                 boxes = face_recognition.face_locations(img)
#                 if boxes:  # Only proceed if faces are found
#                     encodes_cur_frame = face_recognition.face_encodings(img, boxes)
#                     if encodes_cur_frame:  # Check if encodings were generated
#                         self.encode_list.append(encodes_cur_frame[0])
#             except Exception as e:
#                 print(f"Error processing image: {str(e)}")
#                 continue

#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(40)  # 25 FPS (1000ms/40ms = 25)

#     def face_rec_(self, frame, encode_list_known, class_names):
#         def mark_attendance(name):
#             if self.ClockInButton.isChecked():
#                 self.ClockInButton.setEnabled(False)
#                 with open('Attendance.csv', 'a') as f:
#                     if name != 'unknown':
#                         buttonReply = QMessageBox.question(self, 'Welcome ' + name, 'Are you Clocking In?',
#                                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#                         if buttonReply == QMessageBox.Yes:
#                             date_time_string = datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S")
#                             f.writelines(f'\n{name},{date_time_string},Clock In')
#                             self.ClockInButton.setChecked(False)
#                             self.NameLabel.setText(name)
#                             self.StatusLabel.setText('Clocked In')
#                             self.HoursLabel.setText('Measuring')
#                             self.MinLabel.setText('')
#                             self.Time1 = datetime.datetime.now()
#                             self.ClockInButton.setEnabled(True)
#                         else:
#                             print('Not clicked.')
#                             self.ClockInButton.setEnabled(True)
#             elif self.ClockOutButton.isChecked():
#                 self.ClockOutButton.setEnabled(False)
#                 with open('Attendance.csv', 'a') as f:
#                     if name != 'unknown':
#                         buttonReply = QMessageBox.question(self, 'Hey ' + name, 'Are you Clocking Out?',
#                                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#                         if buttonReply == QMessageBox.Yes:
#                             date_time_string = datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S")
#                             f.writelines(f'\n{name},{date_time_string},Clock Out')
#                             self.ClockOutButton.setChecked(False)
#                             self.NameLabel.setText(name)
#                             self.StatusLabel.setText('Clocked Out')
#                             self.Time2 = datetime.datetime.now()
#                             self.ElapseList(name)
#                             self.TimeList2.append(datetime.datetime.now())
#                             CheckInTime = self.TimeList1[-1]
#                             CheckOutTime = self.TimeList2[-1]
#                             self.ElapseHours = (CheckOutTime - CheckInTime)
#                             self.MinLabel.setText("{:.0f}".format(abs(self.ElapseHours.total_seconds() / 60) % 60) + 'm')
#                             self.HoursLabel.setText("{:.0f}".format(abs(self.ElapseHours.total_seconds() / 60 ** 2)) + 'h')
#                             self.ClockOutButton.setEnabled(True)
#                         else:
#                             print('Not clicked.')
#                             self.ClockOutButton.setEnabled(True)

#         # Convert frame to RGB
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
#         # Find all face locations and encodings
#         faces_cur_frame = face_recognition.face_locations(rgb_frame)
#         encodes_cur_frame = face_recognition.face_encodings(rgb_frame, faces_cur_frame)

#         for encodeFace, faceLoc in zip(encodes_cur_frame, faces_cur_frame):
#             matches = face_recognition.compare_faces(encode_list_known, encodeFace, tolerance=0.50)
#             face_dis = face_recognition.face_distance(encode_list_known, encodeFace)
#             name = "unknown"
#             best_match_index = np.argmin(face_dis)
#             if matches[best_match_index]:
#                 name = class_names[best_match_index].upper()
#                 y1, x2, y2, x1 = faceLoc
#                 cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                 cv2.rectangle(frame, (x1, y2 - 20), (x2, y2), (0, 255, 0), cv2.FILLED)
#                 cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
#             mark_attendance(name)
#         return frame

#     def update_frame(self):
#         ret, self.image = self.capture.read()
#         if ret:
#             self.displayImage(self.image, self.encode_list, self.class_names, 1)

#     def ElapseList(self, name):
#         with open('Attendance.csv', 'r') as csv_file:
#             csv_reader = csv.reader(csv_file, delimiter=',')
#             for row in csv_reader:
#                 if len(row) >= 2:
#                     if row[0] == name:
#                         if 'Clock In' in row:
#                             Time1 = datetime.datetime.strptime(row[1], '%y/%m/%d %H:%M:%S')
#                             self.TimeList1.append(Time1)
#                         elif 'Clock Out' in row:
#                             Time2 = datetime.datetime.strptime(row[1], '%y/%m/%d %H:%M:%S')
#                             self.TimeList2.append(Time2)

#     def displayImage(self, image, encode_list, class_names, window=1):
#         try:
#             image = cv2.resize(image, (640, 480))
#             image = self.face_rec_(image, encode_list, class_names)
            
#             # Convert to QImage
#             h, w, ch = image.shape
#             bytes_per_line = ch * w
#             qformat = QImage.Format_RGB888 if ch == 3 else QImage.Format_RGBA8888
#             outImage = QImage(image.data, w, h, bytes_per_line, qformat)
#             outImage = outImage.rgbSwapped()

#             if window == 1:
#                 self.imgLabel.setPixmap(QPixmap.fromImage(outImage))
#                 self.imgLabel.setScaledContents(True)
#         except Exception as e:
#             print(f"Display error: {str(e)}")


from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QTimer, QDate, Qt
from PyQt5.QtWidgets import QDialog, QMessageBox
import cv2
import face_recognition
import numpy as np
import datetime
import os
import csv
from PIL import Image as PILImage

class Ui_OutputDialog(QDialog):
    def __init__(self):
        super(Ui_OutputDialog, self).__init__()
        self.encode_list = None
        self.class_names = None
        loadUi("./outputwindow.ui", self)

        now = QDate.currentDate()
        current_date = now.toString('ddd dd MMMM yyyy')
        current_time = datetime.datetime.now().strftime("%I:%M %p")

        self.Datelabel.setText(current_date)
        self.Timelabel.setText(current_time)
        self.image = None

    @pyqtSlot()
    def startVideo(self, camera_name):
        if len(camera_name) == 1:
            self.capture = cv2.VideoCapture(int(camera_name))
        else:
            self.capture = cv2.VideoCapture(camera_name)
        self.timer = QTimer(self)
        path = 'ImagesAttendance'
        if not os.path.exists(path):
            os.mkdir(path)

        images = []
        self.class_names = []
        self.encode_list = []
        self.TimeList1 = []
        self.TimeList2 = []
        attendance_list = os.listdir(path)

        for cl in attendance_list:
            img_path = os.path.join(path, cl)
            try:
                pil_img = PILImage.open(img_path).convert('RGB')
                img_array = np.array(pil_img)
                img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
                rgb_img = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
                images.append(rgb_img)
                self.class_names.append(os.path.splitext(cl)[0])
            except Exception as e:
                print(f"Error loading image {cl}: {str(e)}")
                continue

        for img in images:
            try:
                if img.dtype != np.uint8:
                    img = img.astype(np.uint8)
                boxes = face_recognition.face_locations(img)
                if boxes:
                    encodes_cur_frame = face_recognition.face_encodings(img, boxes)
                    if encodes_cur_frame:
                        self.encode_list.append(encodes_cur_frame[0])
            except Exception as e:
                print(f"Error processing image: {str(e)}")
                continue

        self.timer.timeout.connect(self.update_frame)
        self.timer.start(40)

    def face_rec_(self, frame, encode_list_known, class_names):
        def mark_attendance(name):
            if self.ClockInButton.isChecked():
                self.ClockInButton.setEnabled(False)
                with open('Attendance.csv', 'a') as f:
                    if name != 'unknown':
                        buttonReply = QMessageBox.question(self, 'Welcome ' + name, 'Are you Clocking In?',
                                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if buttonReply == QMessageBox.Yes:
                            date_time_string = datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S")
                            f.writelines(f'\n{name},{date_time_string},Clock In')
                            self.ClockInButton.setChecked(False)
                            self.NameLabel.setText(name)
                            self.StatusLabel.setText('Clocked In')
                            self.HoursLabel.setText('Measuring')
                            self.MinLabel.setText('')
                            self.Time1 = datetime.datetime.now()
                            self.ClockInButton.setEnabled(True)
                        else:
                            print('Not clicked.')
                            self.ClockInButton.setEnabled(True)
            elif self.ClockOutButton.isChecked():
                self.ClockOutButton.setEnabled(False)
                with open('Attendance.csv', 'a') as f:
                    if name != 'unknown':
                        buttonReply = QMessageBox.question(self, 'Hey ' + name, 'Are you Clocking Out?',
                                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if buttonReply == QMessageBox.Yes:
                            date_time_string = datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S")
                            f.writelines(f'\n{name},{date_time_string},Clock Out')
                            self.ClockOutButton.setChecked(False)
                            self.NameLabel.setText(name)
                            self.StatusLabel.setText('Clocked Out')
                            self.Time2 = datetime.datetime.now()
                            self.ElapseList(name)
                            self.TimeList2.append(datetime.datetime.now())
                            CheckInTime = self.TimeList1[-1]
                            CheckOutTime = self.TimeList2[-1]
                            self.ElapseHours = (CheckOutTime - CheckInTime)
                            self.MinLabel.setText("{:.0f}".format(abs(self.ElapseHours.total_seconds() / 60) % 60) + 'm')
                            self.HoursLabel.setText("{:.0f}".format(abs(self.ElapseHours.total_seconds() / 3600)) + 'h')
                            self.ClockOutButton.setEnabled(True)
                        else:
                            print('Not clicked.')
                            self.ClockOutButton.setEnabled(True)

        try:
            if frame.dtype != np.uint8:
                frame = frame.astype(np.uint8)
            if len(frame.shape) != 3 or frame.shape[2] != 3:
                frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faces_cur_frame = face_recognition.face_locations(rgb_frame)
            encodes_cur_frame = face_recognition.face_encodings(rgb_frame, faces_cur_frame)

            for encodeFace, faceLoc in zip(encodes_cur_frame, faces_cur_frame):
                matches = face_recognition.compare_faces(encode_list_known, encodeFace, tolerance=0.50)
                face_dis = face_recognition.face_distance(encode_list_known, encodeFace)
                name = "unknown"
                best_match_index = np.argmin(face_dis)
                if matches[best_match_index]:
                    name = class_names[best_match_index].upper()
                    y1, x2, y2, x1 = faceLoc
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(frame, (x1, y2 - 20), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                mark_attendance(name)
        except Exception as e:
            print(f"Error in face recognition: {e}")
        return frame

    def update_frame(self):
        ret, self.image = self.capture.read()
        if ret:
            if self.image.dtype != np.uint8:
                self.image = self.image.astype(np.uint8)
            if len(self.image.shape) != 3 or self.image.shape[2] != 3:
                self.image = cv2.cvtColor(self.image, cv2.COLOR_GRAY2BGR)
            self.displayImage(self.image, self.encode_list, self.class_names, 1)

    def ElapseList(self, name):
        with open('Attendance.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if len(row) >= 2:
                    if row[0] == name:
                        if 'Clock In' in row:
                            Time1 = datetime.datetime.strptime(row[1], '%y/%m/%d %H:%M:%S')
                            self.TimeList1.append(Time1)
                        elif 'Clock Out' in row:
                            Time2 = datetime.datetime.strptime(row[1], '%y/%m/%d %H:%M:%S')
                            self.TimeList2.append(Time2)

    def displayImage(self, image, encode_list, class_names, window=1):
        try:
            image = cv2.resize(image, (640, 480))
            image = self.face_rec_(image, encode_list, class_names)

            h, w, ch = image.shape
            bytes_per_line = ch * w
            qformat = QImage.Format_RGB888 if ch == 3 else QImage.Format_Indexed8
            outImage = QImage(image.data, w, h, bytes_per_line, qformat)
            outImage = outImage.rgbSwapped()

            if window == 1:
                self.imgLabel.setPixmap(QPixmap.fromImage(outImage))
                self.imgLabel.setScaledContents(True)
        except Exception as e:
            print(f"Display error: {str(e)}")
