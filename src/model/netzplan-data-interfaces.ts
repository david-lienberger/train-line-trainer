export interface Origin {
	label: string;
}

export interface LineflowStop {
	station_code: string;
	station_label: string;
	departure_minute: string;
	arrival_minute: string;
	is_origin: boolean;
	is_departure: boolean;
}

export interface Basetact {
	interval_minutes: number;
	departure_minutes: string;
	lineflowstops: LineflowStop[];
}

export interface Line {
	label: string;
	color: string;
	station_code_max_stretch_1: string;
	station_code_max_stretch_2: string;
	basetacts: Basetact[];
}

export interface General {
	all_lines: Line[];
}

export interface NetzplanData {
	origins: Record<string, Origin>[];
	general: General;
}
