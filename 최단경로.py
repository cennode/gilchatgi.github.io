import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import networkx as nx


classroom_coords = {

#1층 장소
    '진로활동실': (260, 390, '1F'), '진로상담실': (290, 390, '1F'), '남교사휴게실': (315, 390, '1F'), '보건실': (345, 390, '1F'),
    '특수반': (405, 390, '1F'), '교장실': (450, 390, '1F'), '행정실': (490, 390, '1F'), '본관입구': (535, 390, '1F'),
    '1교무실': (610, 390, '1F'), '신발장1': (195, 345, '1F'), '신발장2': (715, 390, '1F'), '여교사휴게실': (735, 390, '1F'), 'wee 클래스': (765, 420, '1F'),
    '시청각실': (95, 205, '1F'), '준비실': (60, 250, '1F'), '문서고': (65, 390, '1F'), '학력향상실':(135, 345, '1F'),
    '학교운영위원회실':(170,345, '1F'),

    #1층 복도 지점들
    '복도-73': (95, 250, '1F'), '복도-74': (95, 280, '1F'), '복도-75': (95, 390, '1F'),
    '복도-76': (135, 390, '1F'), '복도-77': (170, 390, '1F'), '복도-78': (195, 390, '1F'),
    '복도-79': (220, 390, '1F'), '복도-80': (220, 420, '1F'), '복도-81': (260, 420, '1F'),
    '복도-82': (290, 420, '1F'), '복도-83': (315, 420, '1F'), '복도-84': (345, 420, '1F'),
    '복도-85': (375, 420, '1F'), '복도-86': (405, 420, '1F'), '복도-87': (450, 420, '1F'),
    '복도-88': (490, 420,'1F'), '복도-89': (535,420,'1F'),
    '복도-91': (690,420,'1F'), '복도-92': (715,420,'1F'), '복도-93': (735,420,'1F'),
    '복도-90': (610, 420, '1F'),

    # 1층 계단
    '계단11': (25, 280, '1F'),
    '계단12': (220, 345, '1F'),
    '계단13': (375, 345, '1F'),
    '계단14': (535, 455, '1F'),
    '계단15': (690, 345, '1F'),

    # --- 2층 장소들 ---
    '1-1': (765, 390, '2F'), '1-2': (720, 390, '2F'), '1-3': (660, 390, '2F'), '1-4': (615, 390, '2F'),
    '1-5': (490, 390, '2F'), '1-6': (450, 390, '2F'), '1-7': (405, 390, '2F'), '1-8': (350, 390, '2F'),
    '1-9': (305, 390, '2F'), '1-10': (255, 390, '2F'), '방송실': (570, 390, '2F'), '제2교무실': (535, 390, '2F'),
    '홈베이스-1': (175, 345, '2F'), '홈베이스-2': (135, 345, '2F'), '화학생물실': (65, 390, '2F'),
    '학생활동실5': (65, 330, '2F'), '컴퓨터실': (65, 245, '2F'), 'ai융합실': (100, 165, '2F'),

    # 2층 복도 지점들
    '복도-1': (100, 245, '2F'), '복도-2': (100, 285, '2F'), '복도-3': (100, 330, '2F'),
    '복도-4': (100, 390, '2F'), '복도-5': (135, 390, '2F'), '복도-6': (175, 390, '2F'),
    '복도-7': (215, 390, '2F'), '복도-8': (215, 420, '2F'), '복도-9': (255, 420, '2F'),
    '복도-10': (305, 420, '2F'), '복도-11': (350, 420, '2F'), '복도-12': (375, 420, '2F'),
    '복도-13': (405, 420, '2F'), '복도-14': (450, 420, '2F'), '복도-15': (490, 420, '2F'), '복도-03': (535, 420, '2F'),
    '복도-16': (545, 420, '2F'), '복도-17': (570, 420, '2F'), '복도-18': (615, 420, '2F'),
    '복도-19': (660, 420, '2F'), '복도-20': (690, 420, '2F'), '복도-01': (720, 420, '2F'),
    '복도-02': (765, 420, '2F'),

    # 2층 계단
    '계단21': (30, 285, '2F'),
    '계단22': (215, 335, '2F'),
    '계단23': (375, 345, '2F'),
    '계단24': (545, 455, '2F'),
    '계단25': (690, 345, '2F'),

    # --- 3층 장소들 ---
    '2-1': (715, 400, '3F'), '2-2': (650, 400, '3F'), '2-3': (605, 400, '3F'), '2-4': (570, 400, '3F'),
    '2-5': (480, 400, '3F'), '2-6': (435, 400, '3F'), '2-7': (400, 400, '3F'), '2-8': (335, 400, '3F'),
    '2-9': (290, 400, '3F'), '2-10': (245, 400, '3F'), '3교무실': (535, 400, '3F'), '4교무실': (763, 420, '3F'),
    '홈베이스-3': (135, 370, '3F'), '홈베이스-4': (180, 370, '3F'), '물리지구과학실': (75, 390, '3F'),
    '학생활동실4': (75, 345, '3F'), '학습실': (75, 255, '3F'), '도서열람실': (100, 185, '3F'),

    # 3층 복도 지점들
    '복도-21': (100, 255, '3F'), '복도-22': (100, 285, '3F'), '복도-23': (100, 345, '3F'),
    '복도-24': (100, 390, '3F'), '복도-25': (135, 390, '3F'), '복도-26': (180, 390, '3F'),
    '복도-27': (215, 390, '3F'), '복도-28': (215, 420, '3F'), '복도-29': (245, 420, '3F'),
    '복도-30': (290, 420, '3F'), '복도-31': (335, 420, '3F'), '복도-32': (380, 420, '3F'),
    '복도-33': (400, 420, '3F'), '복도-34': (435, 420, '3F'), '복도-35': (480, 420, '3F'),
    '복도-36': (530, 420, '3F'), '복도-37': (545, 420, '3F'), '복도-38': (570, 420, '3F'),
    '복도-39': (605, 420, '3F'), '복도-40': (650, 420, '3F'), '복도-41': (690, 420, '3F'),
    '복도-42': (715, 420, '3F'),

    # 3층 계단
    '계단31': (690, 350, '3F'),
    '계단32': (545, 460, '3F'),
    '계단33': (380, 350, '3F'),
    '계단34': (215, 335, '3F'),
    '계단35': (30, 285, '3F'),

    # ---4층 장소들---
    '3-1': (715, 400, '4F'), '3-2': (650, 400, '4F'), '3-3': (605, 400, '4F'), '3-4': (570, 400, '4F'),
    '3-5': (480, 400, '4F'), '3-6': (435, 400, '4F'), '3-7': (400, 400, '4F'), '3-8': (335, 400, '4F'),
    '3-9': (290, 400, '4F'), '3-10': (245, 400, '4F'), '학생활동실3': (535, 400, '4F'), '제5교무실': (763, 420, '4F'),
    '홈베이스-5': (135, 370, '4F'), '홈베이스-6': (180, 370, '4F'), '미술실': (75, 390, '4F'),
    '미술준비실': (75, 345, '4F'), '학생회실': (75, 255, '4F'), '학생활동실2': (100, 185, '4F'), '음악실': (100, 165, '4F'),

    # 4층 복도 지점들
    '복도-51': (100, 255, '4F'), '복도-52': (100, 285, '4F'), '복도-53': (100, 345, '4F'),
    '복도-54': (100, 390, '4F'), '복도-55': (135, 390, '4F'), '복도-56': (180, 390, '4F'),
    '복도-57': (215, 390, '4F'), '복도-58': (215, 420, '4F'), '복도-59': (245, 420, '4F'),
    '복도-60': (290, 420, '4F'), '복도-61': (335, 420, '4F'), '복도-62': (380, 420, '4F'),
    '복도-63': (400, 420, '4F'), '복도-64': (435, 420, '4F'), '복도-65': (480, 420, '4F'),
    '복도-66': (530, 420, '4F'), '복도-67': (545, 420, '4F'), '복도-68': (570, 420, '4F'),
    '복도-69': (605, 420, '4F'), '복도-70': (650, 420, '4F'), '복도-71': (690, 420, '4F'),
    '복도-72': (715, 420, '4F'),

    # 4층 계단
    '계단41': (690, 350, '4F'),
    '계단42': (545, 460, '4F'),
    '계단43': (380, 350, '4F'),
    '계단44': (215, 335, '4F'),
    '계단45': (30, 285, '4F')
}


G = nx.Graph()


edges_1f = [
    ('진로활동실', '복도-81'), ('진로상담실', '복도-82'), ('남교사휴게실', '복도-83'), ('보건실', '복도-84'),
    ('특수반', '복도-86'), ('교장실', '복도-87'), ('행정실', '복도-88'), ('본관입구', '복도-89'),
    ('신발장1', '복도-78'), ('여교사휴게실', '복도-93'), ('신발장2', '복도-92'),
    ('시청각실', '복도-73'), ('준비실', '복도-73'), ('문서고', '복도-75'), ('학력향상실', '복도-76'),
    ('학교운영위원회실', '복도-77'),('wee 클래스', '복도-93'),

    ('복도-73', '복도-74'), ('복도-74', '복도-75'), ('복도-75', '복도-76'), ('복도-76', '복도-77'),
    ('복도-77', '복도-78'), ('복도-78', '복도-79'), ('복도-79', '복도-80'), ('복도-80', '복도-81'),
    ('복도-81', '복도-82'), ('복도-82', '복도-83'), ('복도-83', '복도-84'), ('복도-84', '복도-85'),
    ('복도-85', '복도-86'), ('복도-86', '복도-87'), ('복도-87', '복도-88'), ('복도-88', '복도-89'),
    ('복도-91', '복도-92'), ('복도-92', '복도-93'),
    ('복도-79', '복도-78'),
    ('복도-85', '복도-84'),
    ('복도-89', '복도-88'),
    ('복도-74', '복도-73'),


    ('계단11', '복도-74'),
    ('계단12', '복도-79'),
    ('계단13', '복도-85'),
    ('계단14', '복도-89'),
    ('계단15', '복도-91'),
]

edges_2f = [
    ('1-1', '복도-02'), ('1-2', '복도-01'), ('1-3', '복도-19'), ('1-4', '복도-18'),
    ('1-5', '복도-15'), ('1-6', '복도-14'), ('1-7', '복도-13'), ('1-8', '복도-11'),
    ('1-9', '복도-10'), ('1-10', '복도-9'), ('제2교무실', '복도-03'), ('방송실', '복도-17'),
    ('홈베이스-1', '복도-6'), ('홈베이스-2', '복도-5'), ('화학생물실', '복도-4'),
    ('학생활동실5', '복도-3'), ('컴퓨터실', '복도-1'), ('ai융합실', '복도-1'),

    ('복도-1', '복도-2'), ('복도-2', '복도-3'), ('복도-3', '복도-4'), ('복도-4', '복도-5'),
    ('복도-5', '복도-6'), ('복도-6', '복도-7'), ('복도-7', '복도-8'), ('복도-8', '복도-9'),
    ('복도-9', '복도-10'), ('복도-10', '복도-11'), ('복도-11', '복도-12'), ('복도-12', '복도-13'),
    ('복도-13', '복도-14'), ('복도-14', '복도-15'), ('복도-03', '복도-16'), ('복도-16', '복도-17'),
    ('복도-17', '복도-18'), ('복도-18', '복도-19'), ('복도-19', '복도-20'), ('복도-20', '복도-01'),
    ('복도-01', '복도-02'), ('복도-15', '복도-03'),

    # 2층 계단과 복도 연결
    ('계단21', '복도-2'),
    ('계단22', '복도-7'),
    ('계단23', '복도-12'),
    ('계단24', '복도-16'),
    ('계단25', '복도-20'),
]


edges_3f = [
    ('2-1', '복도-42'), ('2-2', '복도-40'), ('2-3', '복도-39'), ('2-4', '복도-38'),
    ('2-5', '복도-35'), ('2-6', '복도-34'), ('2-7', '복도-33'), ('2-8', '복도-31'),
    ('2-9', '복도-30'), ('2-10', '복도-29'), ('3교무실', '복도-37'), ('4교무실', '복도-42'),
    ('홈베이스-3', '복도-25'), ('홈베이스-4', '복도-26'), ('물리지구과학실', '복도-24'),
    ('학생활동실4', '복도-23'), ('학습실', '복도-21'), ('도서열람실', '복도-21'),

    ('복도-21', '복도-22'), ('복도-22', '복도-23'), ('복도-23', '복도-24'), ('복도-24', '복도-25'),
    ('복도-25', '복도-26'), ('복도-26', '복도-27'), ('복도-27', '복도-28'), ('복도-28', '복도-29'),
    ('복도-29', '복도-30'), ('복도-30', '복도-31'), ('복도-31', '복도-32'), ('복도-32', '복도-33'),
    ('복도-33', '복도-34'), ('복도-34', '복도-35'), ('복도-35', '복도-36'), ('복도-36', '복도-37'),
    ('복도-37', '복도-38'), ('복도-38', '복도-39'), ('복도-39', '복도-40'), ('복도-40', '복도-41'),
    ('복도-41', '복도-42'),


    ('계단31', '복도-41'),
    ('계단32', '복도-37'),
    ('계단33', '복도-32'),
    ('계단34', '복도-27'),
    ('계단35', '복도-22'),
]

#
edges_4f = [
    ('3-1', '복도-72'), ('3-2', '복도-70'), ('3-3', '복도-69'), ('3-4', '복도-68'),
    ('3-5', '복도-65'), ('3-6', '복도-64'), ('3-7', '복도-63'), ('3-8', '복도-61'),
    ('3-9', '복도-60'), ('3-10', '복도-59'), ('학생활동실3', '복도-66'), ('제5교무실', '복도-72'),
    ('홈베이스-5', '복도-55'), ('홈베이스-6', '복도-56'), ('미술실', '복도-54'),
    ('미술준비실', '복도-53'), ('학생회실', '복도-51'), ('학생활동실2', '복도-51'), ('음악실', '복도-51'),

    ('복도-51', '복도-52'), ('복도-52', '복도-53'), ('복도-53', '복도-54'), ('복도-54', '복도-55'),
    ('복도-55', '복도-56'), ('복도-56', '복도-57'), ('복도-57', '복도-58'), ('복도-58', '복도-59'),
    ('복도-59', '복도-60'), ('복도-60', '복도-61'), ('복도-61', '복도-62'), ('복도-62', '복도-63'),
    ('복도-63', '복도-64'), ('복도-64', '복도-65'), ('복도-65', '복도-66'), ('복도-66', '복도-67'),
    ('복도-67', '복도-68'), ('복도-68', '복도-69'), ('복도-69', '복도-70'), ('복도-70', '복도-71'),
    ('복도-71', '복도-72'),

    # 4층 계단
    ('계단41', '복도-71'),
    ('계단42', '복도-67'),
    ('계단43', '복도-62'),
    ('계단44', '복도-57'),
    ('계단45', '복도-52'),
]


G.add_edges_from(edges_1f + edges_2f + edges_3f + edges_4f)


stairs_connections = {

    '계단11': '계단21',
    '계단21': '계단11',

    '계단12': '계단22',
    '계단22': '계단12',

    '계단13': '계단23',
    '계단23': '계단13',

    '계단14': '계단24',
    '계단24': '계단14',

    '계단15': '계단25',
    '계단25': '계단15',

    '계단21': '계단35',
    '계단35': '계단21',

    '계단22': '계단34',
    '계단34': '계단22',

    '계단23': '계단33',
    '계단33': '계단23',

    '계단24': '계단32',
    '계단32': '계단24',

    '계단25': '계단31',
    '계단31': '계단25',

    '계단31': '계단41',
    '계단41': '계단31',

    '계단32': '계단42',
    '계단42': '계단32',

    '계단33': '계단43',
    '계단43': '계단33',

    '계단34': '계단44',
    '계단44': '계단34',

    '계단35': '계단45',
    '계단45': '계단35',
}


for stair1, stair2 in stairs_connections.items():
    G.add_edge(stair1, stair2)


floor_maps = {
    '1F': '1st floor.png',
    '2F': '2nd floor.png',
    '3F': '3rd floor.png',
    '4F': '4th floor.png',
}



def find_path_with_floor_change(start_node, end_node):
    """
    출발지와 도착지 노드를 받아 최단 경로를 찾습니다.
    같은 층 내 이동과 층 간 이동(계단 이용)을 모두 고려합니다.
    """

    if start_node not in classroom_coords or end_node not in classroom_coords:
        print(f"오류: '{start_node}' 또는 '{end_node}'가 장소 목록에 없습니다.")
        return None

    try:
        return nx.shortest_path(G, source=start_node, target=end_node)
    except nx.NetworkXNoPath:

        return None
    except Exception as e:
        print(f"경로 탐색 중 오류 발생: {e}")
        return None



class FloorMapApp:
    def __init__(self, root):
        """애플리케이션 초기화: UI 요소 생성 및 초기 설정."""
        self.root = root
        self.root.title("복도 최단 경로 시뮬레이터")

        self.start_var = tk.StringVar()
        self.end_var = tk.StringVar()
        self.current_floor = tk.StringVar(value='1F')


        classroom_only = sorted([
            k for k in classroom_coords
            if not k.startswith("복도") and not k.startswith("계단")
        ])

        # UI 요소 생성 및 배치
        ttk.Label(root, text="출발지:").pack(pady=2)
        self.start_menu = ttk.Combobox(root, textvariable=self.start_var, values=classroom_only, state="readonly")
        self.start_menu.pack(pady=2)
        self.start_menu.set("1-1")

        ttk.Label(root, text="도착지:").pack(pady=2)
        self.end_menu = ttk.Combobox(root, textvariable=self.end_var, values=classroom_only, state="readonly")
        self.end_menu.pack(pady=2)
        self.end_menu.set("1-2")

        ttk.Button(root, text="경로 표시", command=self.show_path).pack(pady=5)


        self.floor_frame = ttk.Frame(root)
        self.floor_frame.pack(pady=10)
        ttk.Label(self.floor_frame, text="현재 층: ").pack(side=tk.LEFT)
        self.current_floor_label = ttk.Label(self.floor_frame, textvariable=self.current_floor,
                                             font=("Helvetica", 16, "bold"))
        self.current_floor_label.pack(side=tk.LEFT)


        ttk.Button(self.floor_frame, text="1층 보기", command=lambda: self.switch_floor('1F')).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.floor_frame, text="2층 보기", command=lambda: self.switch_floor('2F')).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.floor_frame, text="3층 보기", command=lambda: self.switch_floor('3F')).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.floor_frame, text="4층 보기", command=lambda: self.switch_floor('4F')).pack(side=tk.LEFT, padx=5)

        self.canvas = tk.Canvas(root, width=1000, height=600, bg="white")
        self.canvas.pack(pady=10)

        self.full_path = []
        self.load_floor_map(self.current_floor.get())

    def load_floor_map(self, floor):
        """
        주어진 층의 지도 이미지를 로드하여 캔버스에 표시하고,
        현재 층 상태를 업데이트합니다.
        """
        try:
            img = Image.open(floor_maps[floor]).convert("RGBA")

            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()


            if canvas_width < 100 or canvas_height < 100:
                self.root.update_idletasks()
                canvas_width = self.canvas.winfo_width()
                canvas_height = self.canvas.winfo_height()
                if canvas_width < 100 or canvas_height < 100:
                    canvas_width = 1000
                    canvas_height = 600

            img_width, img_height = img.size

            ratio = min(canvas_width / img_width, canvas_height / img_height)
            new_width = int(img_width * ratio)
            new_height = int(img_height * ratio)

            img = img.resize((new_width, new_height), Image.LANCZOS)

            self.current_map_image = ImageTk.PhotoImage(img)

            self.canvas.delete("all")
            self.canvas.create_image(canvas_width / 2, canvas_height / 2, anchor="center", image=self.current_map_image)

            self.current_floor.set(floor)
            self.draw_current_path_segment()
            self.canvas.create_text(
                canvas_width - 20,
                canvas_height - 20,
                text="1층의 경우, 교무실을 통과하지 않고\n2층을 통해서 가주세요",
                fill="black",
                font=("굴림체", 12, "bold"),
                anchor="se"
            )

        except FileNotFoundError:
            print(f"오류: '{floor_maps[floor]}' 파일을 찾을 수 없습니다. 경로를 확인하세요.")
            self.canvas.delete("all")
            self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2,
                                     text=f"오류: '{floor_maps[floor]}' 파일을 찾을 수 없습니다.\n파일 경로를 확인하세요.",
                                     fill="red", font=("Helvetica", 16))
        except Exception as e:
            print(f"이미지 로딩 중 오류 발생: {e}")
            self.canvas.delete("all")
            self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2,
                                     text=f"이미지 로딩 중 오류 발생: {e}",
                                     fill="red", font=("Helvetica", 16))

    def switch_floor(self, new_floor):
        """
        층 전환 버튼 클릭 시 호출됩니다.
        """
        self.load_floor_map(new_floor)

    def show_path(self):
        """
        "경로 표시" 버튼 클릭 시 호출됩니다.
        """
        start = self.start_var.get()
        end = self.end_var.get()

        if not start or not end:
            print("출발지와 도착지를 모두 선택하세요.")
            self.full_path = []
            self.draw_current_path_segment()
            return

        self.full_path = find_path_with_floor_change(start, end)

        if self.full_path is None:
            print("경로가 없습니다. 연결 정보를 확인하세요.")
            self.full_path = []
            self.draw_current_path_segment()
            return

        print("계산된 전체 경로:", self.full_path)

        initial_floor = classroom_coords[start][2]
        self.load_floor_map(initial_floor)

    def draw_current_path_segment(self):
        """
        현재 캔버스에 표시된 층에 해당하는 경로 부분을 그립니다.
        이 함수는 지도가 전환될 때마다 호출됩니다.
        """
        current_floor_on_canvas = self.current_floor.get()

        try:
            original_img = Image.open(floor_maps[current_floor_on_canvas]).convert("RGBA")

            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            if canvas_width < 100 or canvas_height < 100:
                canvas_width = 1000
                canvas_height = 600

            img_width, img_height = original_img.size
            ratio = min(canvas_width / img_width, canvas_height / img_height)
            new_width = int(img_width * ratio)
            new_height = int(img_height * ratio)
            img = original_img.resize((new_width, new_height), Image.LANCZOS)

        except FileNotFoundError:
            print(f"이미지 파일 '{floor_maps[current_floor_on_canvas]}'을(를) 찾을 수 없습니다.")
            return
        except Exception as e:
            print(f"이미지 로딩 중 오류 발생: {e}")
            return

        draw = ImageDraw.Draw(img)

        if not self.full_path:
            img_tk = ImageTk.PhotoImage(img)
            self.canvas.image = img_tk
            self.canvas.create_image(canvas_width / 2, canvas_height / 2, anchor="center", image=img_tk)
            return

        nodes_on_current_floor = []
        for node_name in self.full_path:
            if node_name not in classroom_coords:
                continue

            if classroom_coords[node_name][2] == current_floor_on_canvas:
                nodes_on_current_floor.append(node_name)


        if len(nodes_on_current_floor) >= 2:
            for i in range(len(nodes_on_current_floor) - 1):
                n1_name = nodes_on_current_floor[i]
                n2_name = nodes_on_current_floor[i + 1]

                if n1_name.startswith("계단") and n2_name.startswith("계단"):
                    continue

                if classroom_coords[n1_name][2] == current_floor_on_canvas and \
                        classroom_coords[n2_name][2] == current_floor_on_canvas:
                    x1_orig, y1_orig, _ = classroom_coords[n1_name]
                    x2_orig, y2_orig, _ = classroom_coords[n2_name]

                    x1 = int(x1_orig * ratio)
                    y1 = int(y1_orig * ratio)
                    x2 = int(x2_orig * ratio)
                    y2 = int(y2_orig * ratio)

                    draw.line((x1, y1, x2, y2), fill='red', width=5)


        for i, node_name in enumerate(self.full_path):
            if node_name not in classroom_coords:
                continue

            nx_orig, ny_orig, node_floor = classroom_coords[node_name]

            if node_floor == current_floor_on_canvas:
                nx = int(nx_orig * ratio)
                ny = int(ny_orig * ratio)


                if i == 0:
                    draw.rectangle([nx - 6, ny - 6, nx + 6, ny + 6], fill="green")
                # 도착지 마커 (빨간색 삼각형)
                elif i == len(self.full_path) - 1:
                    triangle = [(nx, ny - 8), (nx - 6, ny + 6), (nx + 6, ny + 6)]
                    draw.polygon(triangle, fill="red")

                elif node_name in stairs_connections.keys() or node_name in stairs_connections.values():
                    is_transition_stair = False

                    if i + 1 < len(self.full_path) and self.full_path[i + 1] in classroom_coords and \
                            classroom_coords[self.full_path[i + 1]][2] != node_floor:
                        is_transition_stair = True
                    if i > 0 and self.full_path[i - 1] in classroom_coords and \
                            classroom_coords[self.full_path[i - 1]][2] != node_floor:
                        is_transition_stair = True

                    if is_transition_stair:
                        draw.ellipse([nx - 10, ny - 10, nx + 10, ny + 10], fill="blue", outline="darkblue", width=2)


        img_tk = ImageTk.PhotoImage(img)
        self.canvas.image = img_tk
        self.canvas.create_image(canvas_width / 2, canvas_height / 2, anchor="center", image=img_tk)



if __name__ == "__main__":
    root = tk.Tk()
    app = FloorMapApp(root)
    root.mainloop()