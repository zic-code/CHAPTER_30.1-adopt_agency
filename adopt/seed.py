from app import db
from model import Pet

db.drop_all()
db.create_all()

p1 = Pet(name="Browny" ,species= "dog",age = 5,photo_url='https://media.istockphoto.com/id/1188957744/ko/%EC%82%AC%EC%A7%84/%EC%82%AC%EB%9E%91%EC%8A%A4%EB%9F%AC%EC%9A%B4-%ED%98%BC%ED%95%A9-%ED%92%88%EC%A2%85-%EA%B0%95%EC%95%84%EC%A7%80%EC%9D%98-%EC%8A%A4%ED%8A%9C%EB%94%94%EC%98%A4-%EC%83%B7.jpg?s=612x612&w=0&k=20&c=rbhOWlgq2V03VEiJGgMqd4HSJ8ppXbPy1UZTSDppDOY=')
p2 = Pet(name="mitten" ,species= "cat",age = 2,photo_url='https://media.istockphoto.com/id/1325997570/ko/%EC%82%AC%EC%A7%84/%EB%B2%B5%EA%B3%A8-%EA%B3%A0%EC%96%91%EC%9D%B4%EB%8A%94-%EC%86%8C%ED%8C%8C%EC%97%90-%EB%88%84%EC%9B%8C-%EB%AF%B8%EC%86%8C%EB%A5%BC-%EC%A7%80%EC%97%88%EB%8B%A4.jpg?s=612x612&w=0&k=20&c=79sWRUXKScFdi89ovoPwIPERT8tSfoZVbNLbYa9IQOQ=')
p3 = Pet(name="tweety" ,species= "bird",age = 3,photo_url='https://media.istockphoto.com/id/1321898042/ko/%EC%82%AC%EC%A7%84/%EB%A7%89%EB%8C%80%EA%B8%B0%EC%97%90%EC%84%9C-%ED%8F%AC%EC%A6%88%EB%A5%BC-%EC%B7%A8%ED%95%98%EB%8A%94-%ED%8C%8C%EB%9E%80%EC%83%89-%EB%B6%80%EC%8B%B9.jpg?s=2048x2048&w=is&k=20&c=X76C3lPbnjq-TffRYSECf2bCCxHXbEgkR8WAYpKVIMo=')
p3 = Pet(name="bunny" ,species= "rabbit",age = 3,photo_url='https://media.istockphoto.com/id/959866606/ko/%EC%82%AC%EC%A7%84/%ED%86%A0%EB%81%BC-4-%EA%B0%9C%EC%9B%94-%ED%9D%B0%EC%83%89-%EB%B0%B0%EA%B2%BD%EC%97%90-%EC%95%89%EC%95%84.jpg?s=612x612&w=0&k=20&c=ZrTQ_jVG4AjTT5RZ7xqQbdNkUVN3kch7XCxMt1C0Sz8='
,available=False)
db.session.add_all([p1,p2,p3])
db.session.commit()
