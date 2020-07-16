# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Academicstatus(models.Model):
    idacademicstatus = models.IntegerField(db_column='IdAcademicStatus', primary_key=True)  # Field name made lowercase.
    academicstatusname = models.CharField(db_column='AcademicStatusName', max_length=50)  # Field name made lowercase.
    academicstatusshortname = models.CharField(db_column='AcademicStatusShortname', max_length=15)  # Field name made lowercase.
    instituteid = models.IntegerField(db_column='InstituteId')  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    @classmethod
    def create(cls,id,name,sname,instid,language,date,update,enabled,userid):    
        academic=cls(idacademicstatus=id,academicstatusname=name,academicstatusshortname=sname,instituteid=instid,languagecode=language,createddate=date,updateddate=update,enabled=enabled,userid=userid)
        return academic
    class Meta:
        managed = False
        db_table = 'AcademicStatus'


class Accesslog(models.Model):
    idaccesslog = models.BigIntegerField(db_column='IdAccessLog', primary_key=True)  # Field name made lowercase.
    userinfoid = models.ForeignKey('Userinfo', models.DO_NOTHING, db_column='UserInfoId')  # Field name made lowercase.
    accessdate = models.DateTimeField(db_column='AccessDate')  # Field name made lowercase.
    success = models.BooleanField(db_column='Success')  # Field name made lowercase.
    fromip = models.CharField(db_column='FromIp', max_length=70)  # Field name made lowercase.
    agent = models.CharField(db_column='Agent', max_length=100)  # Field name made lowercase.
    device = models.CharField(db_column='Device', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccessLog'


class Assignstudentinfo(models.Model):
    idassignstudentinfo = models.BigIntegerField(db_column='IdAssignStudentInfo', primary_key=True)  # Field name made lowercase.
    coursecontentid = models.ForeignKey('Coursecontent', models.DO_NOTHING, db_column='CourseContentId')  # Field name made lowercase.
    studentinfoid = models.ForeignKey('Studentinfo', models.DO_NOTHING, db_column='StudentInfoId')  # Field name made lowercase.
    submitiondate = models.DateField(db_column='SubmitionDate')  # Field name made lowercase.
    attempt = models.SmallIntegerField(db_column='Attempt')  # Field name made lowercase.
    grade = models.DecimalField(db_column='Grade', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gradeddate = models.DateTimeField(db_column='GradedDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    uploadfileid = models.BigIntegerField(db_column='UploadFileId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AssignStudentInfo'


class Campus(models.Model):
    idcampus = models.AutoField(db_column='idCampus', primary_key=True)  # Field name made lowercase.
    internalcode = models.CharField(db_column='InternalCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    campusname = models.CharField(db_column='CampusName', max_length=45)  # Field name made lowercase.
    campusshortname = models.CharField(db_column='CampusShortname', max_length=15)  # Field name made lowercase.
    instituteid = models.IntegerField(db_column='InstituteId')  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    @classmethod
    def create(cls,id,name,sname,instid,language,date,update,enabled,userid):    
        campus=cls(internalcode=id,campusname=name,campusshortname=sname,instituteid=instid,languagecode=language,createddate=date,updateddate=update,enabled=enabled,userid=userid)
        return campus        
    class Meta:
        managed = False
        db_table = 'Campus'


class Citycode(models.Model):
    idcitycode = models.AutoField(db_column='IdCityCode', primary_key=True)  # Field name made lowercase.
    internalcode = models.CharField(db_column='InternalCode', max_length=15)  # Field name made lowercase.
    citycode = models.CharField(db_column='CityCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cityname = models.CharField(db_column='CityName', max_length=70)  # Field name made lowercase.
    countrycodeid = models.IntegerField(db_column='CountryCodeId')  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    @classmethod
    def create(cls,id,city,name,countryid,language,date,update,enabled,userid):
        city=cls(internalcode=id,citycode=city,cityname=name,countrycodeid=countryid,languagecode=language,createddate=date,updateddate=update,enabled=enabled,userid=userid)
        return city
    class Meta:
        managed = False
        db_table = 'CityCode'


class Commonlog(models.Model):
    idcommonlog = models.BigIntegerField(db_column='IdCommonLog', primary_key=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=70)  # Field name made lowercase.
    serializeddata = models.TextField(db_column='SerializedData')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CommonLog'


class Contactmedia(models.Model):
    idcontactmedia = models.IntegerField(db_column='IdContactMedia', primary_key=True)  # Field name made lowercase.
    medianame = models.CharField(db_column='MediaName', max_length=60)  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10)  # Field name made lowercase.
    crreateddate = models.DateTimeField(db_column='CrreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    @classmethod
    def create(cls,id,name,language,date,update,enabled,userid):
        contact=cls(idcontactmedia=id,medianame=name,languagecode=language,crreateddate=date,updateddate=update,enabled=enabled,userid=userid)
        return contact
    class Meta:
        managed = False
        db_table = 'ContactMedia'


class Contactstatus(models.Model):
    idcontactstatus = models.IntegerField(db_column='idContactStatus', primary_key=True)  # Field name made lowercase.
    statusname = models.CharField(db_column='StatusName', max_length=50)  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactStatus'


class Countrycode(models.Model):
    idcountrycode = models.AutoField(db_column='IdCountryCode', primary_key=True)  # Field name made lowercase.
    internalcode = models.CharField(db_column='InternalCode', max_length=15)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=15)  # Field name made lowercase.
    countryname = models.CharField(db_column='CountryName', max_length=60)  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    @classmethod
    def create(cls,id,countrycode,countryname,languagecode,createddate,updateddate,enabled,userid):
        country=cls(internalcode=id,countrycode=countrycode,countryname=countryname,languagecode=languagecode,createddate=createddate,updateddate=updateddate,enabled=enabled,userid=userid)
        return country
    class Meta:
        managed = False
        db_table = 'CountryCode'


class Course(models.Model):
    idcourse = models.BigIntegerField(db_column='IdCourse', primary_key=True)  # Field name made lowercase.
    internalcode = models.CharField(db_column='InternalCode', max_length=30)  # Field name made lowercase.
    coursename = models.CharField(db_column='CourseName', max_length=250)  # Field name made lowercase.
    courseshortname = models.CharField(db_column='CourseShortName', max_length=50)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate')  # Field name made lowercase.
    platformid = models.ForeignKey('Platform', models.DO_NOTHING, db_column='PlatformId')  # Field name made lowercase.
    schematypeid = models.ForeignKey('Schematype', models.DO_NOTHING, db_column='SchemaTypeId')  # Field name made lowercase.
    schemanumber = models.IntegerField(db_column='SchemaNumber')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    instituteofferid = models.ForeignKey('Instituteoffer', models.DO_NOTHING, db_column='InstituteOfferId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Course'


class Coursecontent(models.Model):
    idcoursecontent = models.BigIntegerField(db_column='IdCourseContent', primary_key=True)  # Field name made lowercase.
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='CourseId')  # Field name made lowercase.
    resourcetypeid = models.ForeignKey('Resourcetype', models.DO_NOTHING, db_column='ResourceTypeId')  # Field name made lowercase.
    block = models.IntegerField(db_column='Block')  # Field name made lowercase.
    resourceinstance = models.IntegerField(db_column='ResourceInstance')  # Field name made lowercase.
    resourcename = models.CharField(db_column='ResourceName', max_length=250)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate')  # Field name made lowercase.
    grade = models.IntegerField(db_column='Grade')  # Field name made lowercase.
    apply = models.BooleanField(db_column='Apply')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CourseContent'


class Coursecontentgrade(models.Model):
    idcoursecontentgrade = models.BigIntegerField(db_column='IdCourseContentGrade', primary_key=True)  # Field name made lowercase.
    coursecontentid = models.ForeignKey(Coursecontent, models.DO_NOTHING, db_column='CourseContentId')  # Field name made lowercase.
    teacherid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='TeacherId')  # Field name made lowercase.
    studentinfoid = models.ForeignKey('Studentinfo', models.DO_NOTHING, db_column='StudentInfoId')  # Field name made lowercase.
    grade = models.DecimalField(db_column='Grade', max_digits=5, decimal_places=2)  # Field name made lowercase.
    gradeddate = models.DateField(db_column='GradedDate')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CourseContentGrade'


class Coursegrade(models.Model):
    idcoursegrade = models.BigIntegerField(db_column='IdCourseGrade', primary_key=True)  # Field name made lowercase.
    studentinfoid = models.ForeignKey('Studentinfo', models.DO_NOTHING, db_column='StudentInfoId')  # Field name made lowercase.
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='CourseId')  # Field name made lowercase.
    gradetypeid = models.ForeignKey('Gradetype', models.DO_NOTHING, db_column='GradeTypeId')  # Field name made lowercase.
    grade = models.DecimalField(db_column='Grade', max_digits=6, decimal_places=2)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CourseGrade'


class Documentation(models.Model):
    iddocumentation = models.AutoField(db_column='IdDocumentation', primary_key=True)  # Field name made lowercase.
    internalcode = models.CharField(db_column='InternalCode', max_length=15)  # Field name made lowercase.
    namedocument = models.CharField(db_column='NameDocument', max_length=150)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=15)  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Documentation'


class Educationlevel(models.Model):
    ideducationlevel = models.IntegerField(db_column='IdEducationLevel', primary_key=True)  # Field name made lowercase.
    educationlevelname = models.CharField(db_column='EducationLevelName', max_length=80)  # Field name made lowercase.
    educationlevelshortname = models.CharField(db_column='EducationLevelShortname', max_length=20)  # Field name made lowercase.
    instituteid = models.IntegerField(db_column='InstituteId')  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EducationLevel'


class Enrollmentstudentinfo(models.Model):
    idenrollmentstudentinfo = models.BigIntegerField(db_column='IdEnrollmentStudentInfo', primary_key=True)  # Field name made lowercase.
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='CourseId')  # Field name made lowercase.
    studentinfoid = models.ForeignKey('Studentinfo', models.DO_NOTHING, db_column='StudentInfoId')  # Field name made lowercase.
    enrollmentteacherid = models.ForeignKey('Enrollmentteacher', models.DO_NOTHING, db_column='EnrollmentTeacherId')  # Field name made lowercase.
    enrolleddate = models.DateTimeField(db_column='EnrolledDate')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    uploadfileid = models.ForeignKey('Uploadfile', models.DO_NOTHING, db_column='UploadFileId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EnrollmentStudentInfo'


class Enrollmentteacher(models.Model):
    idenrollmentteacher = models.BigIntegerField(db_column='IdEnrollmentTeacher', primary_key=True)  # Field name made lowercase.
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='CourseId')  # Field name made lowercase.
    teacherid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='TeacherId')  # Field name made lowercase.
    enrolleddate = models.DateTimeField(db_column='EnrolledDate')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    uploadfileid = models.ForeignKey('Uploadfile', models.DO_NOTHING, db_column='UploadFileId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EnrollmentTeacher'


class Faculty(models.Model):
    idfaculty = models.IntegerField(db_column='idFaculty', primary_key=True)  # Field name made lowercase.
    facultyname = models.CharField(db_column='FacultyName', max_length=100)  # Field name made lowercase.
    facultyshortname = models.CharField(db_column='FacultyShortname', max_length=15)  # Field name made lowercase.
    instituteofferid = models.ForeignKey('Instituteoffer', models.DO_NOTHING, db_column='InstituteOfferId')  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Faculty'


class Facultycourse(models.Model):
    idfacultycourse = models.BigIntegerField(db_column='idFacultyCourse', primary_key=True)  # Field name made lowercase.
    facultyid = models.ForeignKey(Faculty, models.DO_NOTHING, db_column='FacultyId')  # Field name made lowercase.
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='CourseId')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FacultyCourse'


class Feedbackstudentinfo(models.Model):
    idfeedbackstudentinfo = models.BigIntegerField(db_column='IdFeedbackStudentInfo', primary_key=True)  # Field name made lowercase.
    coursecontentid = models.ForeignKey(Coursecontent, models.DO_NOTHING, db_column='CourseContentId')  # Field name made lowercase.
    studentinfoid = models.ForeignKey('Studentinfo', models.DO_NOTHING, db_column='StudentInfoId')  # Field name made lowercase.
    completed = models.BooleanField(db_column='Completed')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    uploadfileid = models.ForeignKey('Uploadfile', models.DO_NOTHING, db_column='UploadFileId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FeedbackStudentInfo'


class Follows(models.Model):
    idfollow = models.BigIntegerField(db_column='idFollow', primary_key=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    contactmediaid = models.ForeignKey(Contactmedia, models.DO_NOTHING, db_column='ContactMediaId')  # Field name made lowercase.
    contactstatusid = models.ForeignKey(Contactstatus, models.DO_NOTHING, db_column='ContactStatusId')  # Field name made lowercase.
    studentinfoid = models.ForeignKey('Studentinfo', models.DO_NOTHING, db_column='StudentInfoId')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Follows'


class Forumstudentinfo(models.Model):
    idforumstudentinfo = models.BigIntegerField(db_column='IdForumStudentInfo', primary_key=True)  # Field name made lowercase.
    coursecontentid = models.ForeignKey(Coursecontent, models.DO_NOTHING, db_column='CourseContentId')  # Field name made lowercase.
    studentinfoid = models.ForeignKey('Studentinfo', models.DO_NOTHING, db_column='StudentInfoId')  # Field name made lowercase.
    ispost = models.BooleanField(db_column='IsPost')  # Field name made lowercase.
    internparticipationdate = models.IntegerField(db_column='InternParticipationDate')  # Field name made lowercase.
    participationdate = models.DateTimeField(db_column='ParticipationDate')  # Field name made lowercase.
    participationgrade = models.DecimalField(db_column='ParticipationGrade', max_digits=6, decimal_places=2)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    gradeddate = models.DateTimeField(db_column='GradedDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    uploadfileid = models.ForeignKey('Uploadfile', models.DO_NOTHING, db_column='UploadFileId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ForumStudentInfo'


class Funding(models.Model):
    idfunding = models.IntegerField(db_column='IdFunding', primary_key=True)  # Field name made lowercase.
    fundingname = models.CharField(db_column='FundingName', max_length=50)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Funding'


class Gender(models.Model):
    idgender = models.IntegerField(db_column='IdGender', primary_key=True)  # Field name made lowercase.
    gendername = models.CharField(db_column='GenderName', max_length=30)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gender'


class Gradetype(models.Model):
    idgradetype = models.IntegerField(db_column='IdGradeType', primary_key=True)  # Field name made lowercase.
    gradetypename = models.CharField(db_column='GradeTypeName', max_length=50)  # Field name made lowercase.
    gradetypeshortname = models.CharField(db_column='GradeTypeShortname', max_length=15)  # Field name made lowercase.
    instituteid = models.IntegerField(db_column='InstituteId')  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GradeType'


class Groupoffer(models.Model):
    idgroupoffer = models.BigIntegerField(db_column='IdGroupOffer', primary_key=True)  # Field name made lowercase.
    instituteofferid = models.ForeignKey('Instituteoffer', models.DO_NOTHING, db_column='InstituteOfferId')  # Field name made lowercase.
    parentcampusnumber = models.IntegerField(db_column='ParentCampusNumber')  # Field name made lowercase.
    parentcampusname = models.CharField(db_column='ParentCampusName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=25)  # Field name made lowercase.
    cohort = models.DateField(db_column='Cohort')  # Field name made lowercase.
    groupfee = models.DecimalField(db_column='GroupFee', max_digits=12, decimal_places=2)  # Field name made lowercase.
    groupfeere = models.DecimalField(db_column='GroupFeeRe', max_digits=12, decimal_places=2)  # Field name made lowercase.
    numberpayments = models.SmallIntegerField(db_column='NumberPayments')  # Field name made lowercase.
    renumber = models.SmallIntegerField(db_column='ReNumber')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroupOffer'


class Institute(models.Model):
    idinstitute = models.AutoField(db_column='IdInstitute', primary_key=True)  # Field name made lowercase.
    institutename = models.CharField(db_column='InstituteName', max_length=100)  # Field name made lowercase.
    instituteshortname = models.CharField(db_column='InstituteShortName', max_length=20)  # Field name made lowercase.
    instituteaddress = models.CharField(db_column='InstituteAddress', max_length=120)  # Field name made lowercase.
    pathlogo = models.CharField(db_column='PathLogo', max_length=90, blank=True, null=True)  # Field name made lowercase.
    countrycodeid = models.IntegerField(db_column='CountryCodeId')  # Field name made lowercase.
    regioncode = models.CharField(db_column='RegionCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    timezone = models.CharField(db_column='TimeZone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=15)  # Field name made lowercase.
    adminuser = models.IntegerField(db_column='AdminUser')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Institute'


class Instituteoffer(models.Model):
    idinstituteoffer = models.BigIntegerField(db_column='IdInstituteOffer', primary_key=True)  # Field name made lowercase.
    instituteid = models.IntegerField(db_column='InstituteId')  # Field name made lowercase.
    modalityid = models.ForeignKey('Modality', models.DO_NOTHING, db_column='ModalityId')  # Field name made lowercase.
    levelid = models.ForeignKey('Level', models.DO_NOTHING, db_column='LevelId')  # Field name made lowercase.
    campusid = models.ForeignKey(Campus, models.DO_NOTHING, db_column='CampusId')  # Field name made lowercase.
    programid = models.ForeignKey('Program', models.DO_NOTHING, db_column='ProgramId')  # Field name made lowercase.
    acreditationtype = models.CharField(db_column='AcreditationType', max_length=30)  # Field name made lowercase.
    acreditationcode = models.CharField(db_column='AcreditationCode', max_length=40)  # Field name made lowercase.
    acreditationactive = models.BooleanField(db_column='AcreditationActive')  # Field name made lowercase.
    responsableuserid = models.IntegerField(db_column='ResponsableUserId')  # Field name made lowercase.
    schematypeid = models.ForeignKey('Schematype', models.DO_NOTHING, db_column='SchemaTypeId')  # Field name made lowercase.
    schematime = models.IntegerField(db_column='SchemaTime')  # Field name made lowercase.
    grademin = models.DecimalField(db_column='GradeMin', max_digits=5, decimal_places=2)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InstituteOffer'


class Invoiceconcept(models.Model):
    idinvoiceconcept = models.BigAutoField(db_column='IdInvoiceConcept', primary_key=True)  # Field name made lowercase.
    internalcode = models.CharField(db_column='InternalCode', max_length=30)  # Field name made lowercase.
    conceptname = models.CharField(db_column='ConceptName', max_length=70)  # Field name made lowercase.
    groupconcept = models.IntegerField(db_column='GroupConcept')  # Field name made lowercase.
    coiconcept = models.CharField(db_column='CoiConcept', max_length=70)  # Field name made lowercase.
    coiid = models.IntegerField(db_column='CoiId')  # Field name made lowercase.
    coiaccount = models.CharField(db_column='CoiAccount', max_length=50)  # Field name made lowercase.
    instituteid = models.IntegerField(db_column='InstituteId')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    enabled = models.IntegerField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvoiceConcept'


class Invoicestudentinfo(models.Model):
    idinvoicestudentinfo = models.BigIntegerField(db_column='IdInvoiceStudentInfo', primary_key=True)  # Field name made lowercase.
    studentinfoid = models.ForeignKey('Studentinfo', models.DO_NOTHING, db_column='StudentInfoId')  # Field name made lowercase.
    invoiceconceptid = models.ForeignKey(Invoiceconcept, models.DO_NOTHING, db_column='InvoiceConceptId')  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    month = models.SmallIntegerField(db_column='Month')  # Field name made lowercase.
    invoicecreated = models.DateField(db_column='InvoiceCreated')  # Field name made lowercase.
    invoicepaid = models.DateField(db_column='InvoicePaid', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=12, decimal_places=2)  # Field name made lowercase.
    groupofferid = models.BigIntegerField(db_column='GroupOfferId')  # Field name made lowercase.
    moment = models.SmallIntegerField(db_column='Moment')  # Field name made lowercase.
    internalcode = models.IntegerField(db_column='InternalCode')  # Field name made lowercase.
    paid = models.BooleanField(db_column='Paid')  # Field name made lowercase.
    newentry = models.BooleanField(db_column='NewEntry')  # Field name made lowercase.
    crreateddate = models.DateTimeField(db_column='CrreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvoiceStudentInfo'


class Lessonstudentinfo(models.Model):
    idlessonstudentinfo = models.BigIntegerField(db_column='IdLessonStudentInfo', primary_key=True)  # Field name made lowercase.
    coursecontentid = models.ForeignKey(Coursecontent, models.DO_NOTHING, db_column='CourseContentId')  # Field name made lowercase.
    studentinfoid = models.ForeignKey('Studentinfo', models.DO_NOTHING, db_column='StudentInfoId')  # Field name made lowercase.
    stardate = models.DateField(db_column='StarDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate')  # Field name made lowercase.
    attempt = models.SmallIntegerField(db_column='Attempt')  # Field name made lowercase.
    grade = models.IntegerField(db_column='Grade')  # Field name made lowercase.
    completed = models.BooleanField(db_column='Completed')  # Field name made lowercase.
    approved = models.BooleanField(db_column='Approved')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    uploadfileid = models.ForeignKey('Uploadfile', models.DO_NOTHING, db_column='UploadFileId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LessonStudentInfo'


class Level(models.Model):
    idlevel = models.IntegerField(db_column='IdLevel', primary_key=True)  # Field name made lowercase.
    levelname = models.CharField(db_column='LevelName', max_length=45)  # Field name made lowercase.
    levelshortname = models.CharField(db_column='LevelShortname', max_length=15)  # Field name made lowercase.
    instituteid = models.IntegerField(db_column='InstituteId')  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10)  # Field name made lowercase.
    internalcode = models.CharField(db_column='InternalCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Level'


class Maritalstatus(models.Model):
    idmaritalstatus = models.IntegerField(db_column='idMaritalStatus', primary_key=True)  # Field name made lowercase.
    maritalstatusname = models.CharField(db_column='MaritalStatusName', max_length=50)  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MaritalStatus'


class Menuoption(models.Model):
    idmenuoption = models.IntegerField(db_column='IdMenuOption', primary_key=True)  # Field name made lowercase.
    menuname = models.CharField(db_column='MenuName', max_length=50)  # Field name made lowercase.
    menuoption = models.CharField(db_column='MenuOption', max_length=70)  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    parentmenu = models.IntegerField(db_column='ParentMenu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MenuOption'


class Messages(models.Model):
    idmessage = models.BigIntegerField(db_column='IdMessage', primary_key=True)  # Field name made lowercase.
    messagetypeid = models.SmallIntegerField(db_column='MessageTypeId')  # Field name made lowercase.
    messagename = models.TextField(db_column='MessageName')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Messages'


class Messagessend(models.Model):
    idmessagessend = models.BigIntegerField(db_column='idMessagesSend', primary_key=True)  # Field name made lowercase.
    usersend = models.IntegerField(db_column='UserSend')  # Field name made lowercase.
    messageread = models.DateTimeField(db_column='MessageRead', blank=True, null=True)  # Field name made lowercase.
    messageid = models.BigIntegerField(db_column='MessageId')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MessagesSend'


class Modality(models.Model):
    idmodality = models.AutoField(db_column='IdModality', primary_key=True)  # Field name made lowercase.
    modalityname = models.CharField(db_column='ModalityName', max_length=35)  # Field name made lowercase.
    modalityshortname = models.CharField(db_column='ModalityShortname', max_length=15)  # Field name made lowercase.
    instituteid = models.IntegerField(db_column='InstituteId')  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Modality'


class Notificationreason(models.Model):
    idnotificationreason = models.IntegerField(db_column='IdNotificationReason', primary_key=True)  # Field name made lowercase.
    reasonname = models.CharField(db_column='ReasonName', max_length=50)  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NotificationReason'


class Notifications(models.Model):
    idnotifications = models.BigIntegerField(db_column='IdNotifications', primary_key=True)  # Field name made lowercase.
    notificationdate = models.DateTimeField(db_column='NotificationDate')  # Field name made lowercase.
    notificationreasonid = models.ForeignKey(Notificationreason, models.DO_NOTHING, db_column='NotificationReasonId')  # Field name made lowercase.
    attendeddate = models.DateTimeField(db_column='AttendedDate', blank=True, null=True)  # Field name made lowercase.
    followid = models.BigIntegerField(db_column='FollowId', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    studentinfoid = models.ForeignKey('Studentinfo', models.DO_NOTHING, db_column='StudentInfoId')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Notifications'


class Observations(models.Model):
    idobservation = models.BigIntegerField(db_column='IdObservation', primary_key=True)  # Field name made lowercase.
    observation = models.TextField(db_column='Observation')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    studentinfoid = models.ForeignKey('Studentinfo', models.DO_NOTHING, db_column='StudentInfoId')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Observations'


class Onlinesessionstudentinfo(models.Model):
    idonlinesessionstudentinfo = models.BigIntegerField(db_column='IdOnlineSessionStudentInfo', primary_key=True)  # Field name made lowercase.
    coursecontentid = models.ForeignKey(Coursecontent, models.DO_NOTHING, db_column='CourseContentId')  # Field name made lowercase.
    studentinfoid = models.ForeignKey('Studentinfo', models.DO_NOTHING, db_column='StudentInfoId')  # Field name made lowercase.
    comingdate = models.DateTimeField(db_column='ComingDate')  # Field name made lowercase.
    internalsessioncode = models.IntegerField(db_column='InternalSessionCode')  # Field name made lowercase.
    durationtime = models.TimeField(db_column='DurationTime')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    uploadfileid = models.ForeignKey('Uploadfile', models.DO_NOTHING, db_column='UploadFileId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineSessionStudentInfo'


class Platform(models.Model):
    idplatform = models.IntegerField(db_column='IdPlatform', primary_key=True)  # Field name made lowercase.
    platfomname = models.CharField(db_column='PlatfomName', max_length=50)  # Field name made lowercase.
    platformshortname = models.CharField(db_column='PlatformShortName', max_length=10)  # Field name made lowercase.
    instituteid = models.IntegerField(db_column='InstituteId')  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Platform'


class Program(models.Model):
    idprogram = models.BigAutoField(db_column='idProgram', primary_key=True)  # Field name made lowercase.
    internalcode = models.CharField(db_column='InternalCode', max_length=30)  # Field name made lowercase.
    programname = models.CharField(db_column='ProgramName', max_length=50)  # Field name made lowercase.
    programshortname = models.CharField(db_column='ProgramShortname', max_length=15, blank=True, null=True)  # Field name made lowercase.
    instituteid = models.IntegerField(db_column='InstituteId')  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Program'


class Quizstudentinfo(models.Model):
    idquizstudentinfo = models.BigIntegerField(db_column='IdQuizStudentInfo', primary_key=True)  # Field name made lowercase.
    coursecontentid = models.ForeignKey(Coursecontent, models.DO_NOTHING, db_column='CourseContentId')  # Field name made lowercase.
    studentinfoid = models.ForeignKey('Studentinfo', models.DO_NOTHING, db_column='StudentInfoId')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate')  # Field name made lowercase.
    attempt = models.SmallIntegerField(db_column='Attempt')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=25)  # Field name made lowercase.
    grade = models.DecimalField(db_column='Grade', max_digits=6, decimal_places=2)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    uploadfileid = models.ForeignKey('Uploadfile', models.DO_NOTHING, db_column='UploadFileId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuizStudentInfo'


class Resolution(models.Model):
    idresolution = models.AutoField(db_column='IdResolution', primary_key=True)  # Field name made lowercase.
    internalcode = models.CharField(db_column='InternalCode', max_length=15)  # Field name made lowercase.
    nameresolution = models.CharField(db_column='NameResolution', max_length=50)  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Resolution'


class Resourcetype(models.Model):
    idresourcetype = models.IntegerField(db_column='IdResourceType', primary_key=True)  # Field name made lowercase.
    resourcetypename = models.CharField(db_column='ResourceTypeName', max_length=50)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResourceType'


class Roleinfo(models.Model):
    idroleinfo = models.IntegerField(db_column='IdRoleInfo', primary_key=True)  # Field name made lowercase.
    roleinfoname = models.CharField(db_column='RoleInfoName', max_length=50)  # Field name made lowercase.
    roleinfodescription = models.CharField(db_column='RoleInfoDescription', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoleInfo'


class Rolemenuoption(models.Model):
    idrolemenuoption = models.IntegerField(db_column='IdRoleMenuOption', primary_key=True)  # Field name made lowercase.
    roleinfoid = models.ForeignKey(Roleinfo, models.DO_NOTHING, db_column='RoleInfoId')  # Field name made lowercase.
    menuoptionid = models.ForeignKey(Menuoption, models.DO_NOTHING, db_column='MenuOptionId')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoleMenuOption'


class Schematype(models.Model):
    idschematype = models.IntegerField(db_column='idSchemaType', primary_key=True)  # Field name made lowercase.
    schematypename = models.CharField(db_column='SchemaTypeName', max_length=30)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SchemaType'


class Scormstudentinfo(models.Model):
    idscormstudentinfo = models.BigIntegerField(db_column='IdScormStudentInfo', primary_key=True)  # Field name made lowercase.
    coursecontentid = models.ForeignKey(Coursecontent, models.DO_NOTHING, db_column='CourseContentId')  # Field name made lowercase.
    studentinfoid = models.ForeignKey('Studentinfo', models.DO_NOTHING, db_column='StudentInfoId')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    durationtime = models.TimeField(db_column='DurationTime')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    grade = models.DecimalField(db_column='Grade', max_digits=6, decimal_places=2)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    uploadfileid = models.ForeignKey('Uploadfile', models.DO_NOTHING, db_column='UploadFileId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScormStudentInfo'


class Specialty(models.Model):
    idspecialty = models.BigIntegerField(db_column='idSpecialty', primary_key=True)  # Field name made lowercase.
    specialtyname = models.CharField(db_column='SpecialtyName', max_length=100)  # Field name made lowercase.
    specialtyshortname = models.CharField(db_column='SpecialtyShortname', max_length=25)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    instituteofferid = models.ForeignKey(Instituteoffer, models.DO_NOTHING, db_column='InstituteOfferId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Specialty'


class Studentinfo(models.Model):
    idstudentinfo = models.BigIntegerField(db_column='idStudentInfo', primary_key=True)  # Field name made lowercase.
    internalusername = models.CharField(db_column='InternalUsername', max_length=30)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=60)  # Field name made lowercase.
    picpath = models.CharField(db_column='PicPath', max_length=80, blank=True, null=True)  # Field name made lowercase.
    countrycodeid = models.IntegerField(db_column='CountryCodeId')  # Field name made lowercase.
    citycodeid = models.IntegerField(db_column='CityCodeId')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200)  # Field name made lowercase.
    zipcode = models.IntegerField(db_column='ZipCode')  # Field name made lowercase.
    birthdate = models.DateField(db_column='Birthdate')  # Field name made lowercase.
    nickname = models.CharField(db_column='Nickname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maritalstatusid = models.ForeignKey(Maritalstatus, models.DO_NOTHING, db_column='MaritalStatusId')  # Field name made lowercase.
    genderid = models.ForeignKey(Gender, models.DO_NOTHING, db_column='GenderId')  # Field name made lowercase.
    employmentsituation = models.BooleanField(db_column='EmploymentSituation')  # Field name made lowercase.
    economicdependents = models.IntegerField(db_column='EconomicDependents')  # Field name made lowercase.
    fundingid = models.ForeignKey(Funding, models.DO_NOTHING, db_column='FundingId')  # Field name made lowercase.
    admissiondate = models.DateField(db_column='AdmissionDate')  # Field name made lowercase.
    instituteofferid = models.ForeignKey(Instituteoffer, models.DO_NOTHING, db_column='InstituteOfferId')  # Field name made lowercase.
    academicstatusid = models.ForeignKey(Academicstatus, models.DO_NOTHING, db_column='AcademicStatusId')  # Field name made lowercase.
    zeropromotion = models.BooleanField(db_column='ZeroPromotion')  # Field name made lowercase.
    revalidation = models.BooleanField(db_column='Revalidation')  # Field name made lowercase.
    riskmarkedapp = models.BooleanField(db_column='RiskMarkedApp')  # Field name made lowercase.
    riskmarkeduser = models.BooleanField(db_column='RiskMarkedUser')  # Field name made lowercase.
    droppedout = models.BooleanField(db_column='DroppedOut')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StudentInfo'


class Studentinfocontact(models.Model):
    idstudentcontact = models.BigIntegerField(db_column='IdStudentContact', primary_key=True)  # Field name made lowercase.
    studentinfoid = models.ForeignKey(Studentinfo, models.DO_NOTHING, db_column='StudentInfoId')  # Field name made lowercase.
    contactmediaid = models.ForeignKey(Contactmedia, models.DO_NOTHING, db_column='ContactMediaId')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=50)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StudentInfoContact'


class Subject(models.Model):
    idsubjects = models.BigAutoField(db_column='IdSubjects', primary_key=True)  # Field name made lowercase.
    internalcode = models.CharField(db_column='InternalCode', max_length=15)  # Field name made lowercase.
    subjectname = models.CharField(db_column='SubjectName', max_length=300)  # Field name made lowercase.
    subjectshortname = models.CharField(db_column='SubjectShortname', max_length=150, blank=True, null=True)  # Field name made lowercase.
    subjectcode = models.CharField(db_column='SubjectCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    modalityid = models.IntegerField(db_column='ModalityId')  # Field name made lowercase.
    levelid = models.IntegerField(db_column='LevelId')  # Field name made lowercase.
    campusid = models.IntegerField(db_column='CampusId')  # Field name made lowercase.
    programid = models.BigIntegerField(db_column='ProgramId')  # Field name made lowercase.
    planmaster = models.CharField(db_column='PlanMaster', max_length=5, blank=True, null=True)  # Field name made lowercase.
    semester = models.IntegerField(db_column='Semester')  # Field name made lowercase.
    numorder = models.IntegerField(db_column='NumOrder')  # Field name made lowercase.
    optional = models.IntegerField(db_column='Optional')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Subject'


class Teacher(models.Model):
    idteacher = models.BigAutoField(db_column='IdTeacher', primary_key=True)  # Field name made lowercase.
    instituteid = models.IntegerField(db_column='InstituteId')  # Field name made lowercase.
    internalcode = models.CharField(db_column='InternalCode', max_length=15)  # Field name made lowercase.
    internalusername = models.CharField(db_column='InternalUserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=70)  # Field name made lowercase.
    picpath = models.CharField(db_column='PicPath', max_length=90, blank=True, null=True)  # Field name made lowercase.
    countrycodeid = models.IntegerField(db_column='CountryCodeId', blank=True, null=True)  # Field name made lowercase.
    citycodeid = models.IntegerField(db_column='CityCodeId', blank=True, null=True)  # Field name made lowercase.
    admissiondate = models.DateField(db_column='AdmissionDate', blank=True, null=True)  # Field name made lowercase.
    genderid = models.IntegerField(db_column='GenderId', blank=True, null=True)  # Field name made lowercase.
    typehoursid = models.IntegerField(db_column='TypeHoursId', blank=True, null=True)  # Field name made lowercase.
    hourlysalary = models.DecimalField(db_column='HourlySalary', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Teacher'


class Teachereducation(models.Model):
    idteachereducation = models.BigIntegerField(db_column='IdTeacherEducation', primary_key=True)  # Field name made lowercase.
    teacherid = models.ForeignKey(Teacher, models.DO_NOTHING, db_column='TeacherId')  # Field name made lowercase.
    educationlevelid = models.ForeignKey(Educationlevel, models.DO_NOTHING, db_column='EducationLevelId')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=70)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TeacherEducation'


class Towncode(models.Model):
    idtowncode = models.BigAutoField(db_column='IdTownCode', primary_key=True)  # Field name made lowercase.
    internalcode = models.CharField(db_column='InternalCode', max_length=15)  # Field name made lowercase.
    towncode = models.CharField(db_column='TownCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    townname = models.CharField(db_column='TownName', max_length=70)  # Field name made lowercase.
    citycodeid = models.IntegerField(db_column='CityCodeId')  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TownCode'


class Typehours(models.Model):
    idtypehours = models.IntegerField(db_column='IdTypeHours', primary_key=True)  # Field name made lowercase.
    typehoursname = models.CharField(db_column='TypeHoursName', max_length=50)  # Field name made lowercase.
    typehoursshortname = models.CharField(db_column='TypeHoursShortname', max_length=15)  # Field name made lowercase.
    typehoursnumber = models.IntegerField(db_column='TypeHoursNumber')  # Field name made lowercase.
    instituteid = models.IntegerField(db_column='InstituteId')  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TypeHours'


class Uploadfile(models.Model):
    iduploadfile = models.BigIntegerField(db_column='IdUploadFile', primary_key=True)  # Field name made lowercase.
    filetype = models.CharField(db_column='FileType', max_length=50)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=70)  # Field name made lowercase.
    filenamelocal = models.CharField(db_column='FileNameLocal', max_length=70)  # Field name made lowercase.
    resourcetypeid = models.ForeignKey(Resourcetype, models.DO_NOTHING, db_column='ResourceTypeId')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UploadFile'


class Useraccessinfo(models.Model):
    iduseraccessinfo = models.BigIntegerField(db_column='IdUserAccessInfo', primary_key=True)  # Field name made lowercase.
    userinfoid = models.ForeignKey('Userinfo', models.DO_NOTHING, db_column='UserInfoId')  # Field name made lowercase.
    accessinfo = models.TextField(db_column='AccessInfo')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserAccessInfo'


class Userinfo(models.Model):
    iduserinfo = models.BigIntegerField(db_column='IdUserInfo', primary_key=True)  # Field name made lowercase.
    internalusername = models.CharField(db_column='InternalUserName', max_length=50)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=70)  # Field name made lowercase.
    picpath = models.CharField(db_column='PicPath', max_length=80)  # Field name made lowercase.
    countrycodeid = models.IntegerField(db_column='CountryCodeId')  # Field name made lowercase.
    citycodeid = models.IntegerField(db_column='CityCodeId')  # Field name made lowercase.
    instituteid = models.IntegerField(db_column='InstituteId')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserInfo'


class Userinfocontact(models.Model):
    idusercontact = models.BigIntegerField(db_column='IdUserContact', primary_key=True)  # Field name made lowercase.
    userinfoid = models.ForeignKey(Userinfo, models.DO_NOTHING, db_column='UserInfoId')  # Field name made lowercase.
    contactmediaid = models.ForeignKey(Contactmedia, models.DO_NOTHING, db_column='ContactMediaId')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=50)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserInfoContact'


class Userroleinfo(models.Model):
    iduserroleinfo = models.BigIntegerField(db_column='IdUserRoleInfo', primary_key=True)  # Field name made lowercase.
    userinfoid = models.ForeignKey(Userinfo, models.DO_NOTHING, db_column='UserInfoId')  # Field name made lowercase.
    roleinfoid = models.ForeignKey(Roleinfo, models.DO_NOTHING, db_column='RoleInfoId')  # Field name made lowercase.
    enrolleddate = models.DateTimeField(db_column='EnrolledDate')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserRoleInfo'


class Usertk(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'UserTK'


class Usertkn(models.Model):
    username = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserTKN'


class Usuariostk(models.Model):
    username = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UsuariosTK'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
